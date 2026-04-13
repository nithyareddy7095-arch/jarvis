"""Automated email sender with templating, scheduling, and delivery reporting.

Usage examples:
    python backend/scripts/automated_email_sender.py --config backend/scripts/email_jobs.example.json --dry-run
    python backend/scripts/automated_email_sender.py --config backend/scripts/email_jobs.example.json
"""

from __future__ import annotations

import argparse
import json
import logging
import smtplib
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Any


logger = logging.getLogger("automated_email_sender")


@dataclass(slots=True)
class SMTPConfig:
    host: str
    port: int
    username: str
    password: str
    use_tls: bool = True
    from_email: str = ""


@dataclass(slots=True)
class Recipient:
    name: str
    email: str
    purpose: str
    context: dict[str, Any]


@dataclass(slots=True)
class EmailJob:
    send_at: datetime
    subject_template: str
    body_template: str
    recipients: list[Recipient]


def _render_template(template: str, recipient: Recipient) -> str:
    values = {
        "name": recipient.name,
        "email": recipient.email,
        "purpose": recipient.purpose,
        **recipient.context,
    }
    return template.format_map(values)


def _parse_datetime(raw: str) -> datetime:
    dt = datetime.fromisoformat(raw)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def load_config(path: str) -> tuple[SMTPConfig, list[EmailJob]]:
    config_path = Path(path)
    payload = json.loads(config_path.read_text(encoding="utf-8"))

    smtp_payload = payload["smtp"]
    smtp = SMTPConfig(
        host=smtp_payload["host"],
        port=int(smtp_payload["port"]),
        username=smtp_payload["username"],
        password=smtp_payload["password"],
        use_tls=bool(smtp_payload.get("use_tls", True)),
        from_email=smtp_payload.get("from_email", smtp_payload["username"]),
    )

    jobs: list[EmailJob] = []
    for item in payload["jobs"]:
        recipients: list[Recipient] = []
        for recipient in item["recipients"]:
            recipients.append(
                Recipient(
                    name=recipient["name"],
                    email=recipient["email"],
                    purpose=recipient.get("purpose", "general"),
                    context=recipient.get("context", {}),
                )
            )
        jobs.append(
            EmailJob(
                send_at=_parse_datetime(item["send_at"]),
                subject_template=item["subject_template"],
                body_template=item["body_template"],
                recipients=recipients,
            )
        )

    return smtp, jobs


class EmailSender:
    def __init__(self, smtp: SMTPConfig, dry_run: bool = False):
        self.smtp = smtp
        self.dry_run = dry_run

    def _build_message(self, recipient: Recipient, subject: str, body: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.smtp.from_email
        message["To"] = recipient.email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain", "utf-8"))
        return message

    def send_to_recipient(self, recipient: Recipient, subject_template: str, body_template: str) -> None:
        subject = _render_template(subject_template, recipient)
        body = _render_template(body_template, recipient)

        if self.dry_run:
            logger.info("[DRY RUN] Would send email to %s with subject '%s'", recipient.email, subject)
            return

        message = self._build_message(recipient, subject, body)
        with smtplib.SMTP(self.smtp.host, self.smtp.port, timeout=30) as server:
            if self.smtp.use_tls:
                server.starttls()
            server.login(self.smtp.username, self.smtp.password)
            server.sendmail(self.smtp.from_email, [recipient.email], message.as_string())

        logger.info("Sent email to %s", recipient.email)


def run_scheduler(sender: EmailSender, jobs: list[EmailJob], poll_interval: int = 10) -> dict[str, int]:
    queue = sorted(jobs, key=lambda item: item.send_at)
    report = {"sent": 0, "failed": 0}

    while queue:
        now = datetime.now(tz=timezone.utc)
        next_job = queue[0]

        if next_job.send_at > now:
            sleep_for = min((next_job.send_at - now).total_seconds(), poll_interval)
            time.sleep(max(sleep_for, 0.0))
            continue

        queue.pop(0)
        for recipient in next_job.recipients:
            try:
                sender.send_to_recipient(recipient, next_job.subject_template, next_job.body_template)
                report["sent"] += 1
            except Exception as exc:  # noqa: BLE001
                report["failed"] += 1
                logger.exception("Failed to send email to %s: %s", recipient.email, exc)

    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Automated email sender with scheduling support")
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--dry-run", action="store_true", help="Preview sends without connecting to SMTP")
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=10,
        help="Seconds between schedule checks for pending jobs",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )

    smtp, jobs = load_config(args.config)
    sender = EmailSender(smtp=smtp, dry_run=args.dry_run)

    logger.info("Loaded %d job(s) from config", len(jobs))
    report = run_scheduler(sender=sender, jobs=jobs, poll_interval=args.poll_interval)
    logger.info("Completed all jobs. Sent=%d Failed=%d", report["sent"], report["failed"])

    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
