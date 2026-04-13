from datetime import datetime, timedelta, timezone

from backend.scripts.automated_email_sender import (
    EmailJob,
    EmailSender,
    Recipient,
    SMTPConfig,
    _render_template,
    run_scheduler,
)


def test_render_template_uses_recipient_fields_and_context() -> None:
    recipient = Recipient(
        name="Alex",
        email="alex@example.com",
        purpose="Status update",
        context={"action_item": "Review the report"},
    )

    result = _render_template("Hi {name}, {purpose}. {action_item}", recipient)

    assert result == "Hi Alex, Status update. Review the report"


def test_scheduler_reports_success_and_failure() -> None:
    class StubSender(EmailSender):
        def __init__(self) -> None:
            super().__init__(SMTPConfig("host", 25, "user", "pass"), dry_run=True)

        def send_to_recipient(self, recipient, subject_template, body_template):
            if recipient.email == "fail@example.com":
                raise RuntimeError("send failed")

    now = datetime.now(tz=timezone.utc)
    job = EmailJob(
        send_at=now - timedelta(seconds=1),
        subject_template="Hello {name}",
        body_template="Body",
        recipients=[
            Recipient("Ok", "ok@example.com", "notice", {}),
            Recipient("Fail", "fail@example.com", "notice", {}),
        ],
    )

    report = run_scheduler(sender=StubSender(), jobs=[job], poll_interval=0)

    assert report == {"sent": 1, "failed": 1}
