# Project 2: Automated Email Sender

This project delivers a Python-based email automation utility that supports:

1. Automated email sending via `smtplib`.
2. Per-recipient customization using templates.
3. Scheduled delivery at specific ISO-8601 date-time values.
4. Delivery reporting with failed-send visibility.

## Files

- `backend/scripts/automated_email_sender.py`: Main script.
- `backend/scripts/email_jobs.example.json`: Example config with three recipients.

## How It Works

1. Load SMTP credentials and email jobs from JSON.
2. Parse each job's `send_at` time and sort in chronological order.
3. Wait for each job's scheduled time.
4. Render recipient-specific fields into the subject/body templates.
5. Send with SMTP + TLS (or run in `--dry-run` preview mode).
6. Log results and return non-zero exit code if any send fails.

## Example Run

Preview without sending:

```bash
python backend/scripts/automated_email_sender.py \
  --config backend/scripts/email_jobs.example.json \
  --dry-run
```

Real send:

```bash
python backend/scripts/automated_email_sender.py \
  --config /path/to/your/email_jobs.json
```

## Configuration Format

```json
{
  "smtp": {
    "host": "smtp.gmail.com",
    "port": 587,
    "username": "automation@example.com",
    "password": "app-password",
    "use_tls": true,
    "from_email": "automation@example.com"
  },
  "jobs": [
    {
      "send_at": "2026-04-13T12:00:00+00:00",
      "subject_template": "Update for {name}: {purpose}",
      "body_template": "Hello {name}... {action_item}",
      "recipients": [
        {
          "name": "Alex Chen",
          "email": "alex.chen@example.com",
          "purpose": "Quarterly account review",
          "context": {
            "action_item": "Please confirm your preferred meeting slot"
          }
        }
      ]
    }
  ]
}
```

## Template Variables

Built-in placeholders:

- `{name}`
- `{email}`
- `{purpose}`

And any keys inside each recipient `context` object (for example `{action_item}`).

## Error Handling and Notifications

- Failed sends are caught and logged with recipient + error details.
- Scheduler continues processing remaining recipients/jobs.
- Final report prints `Sent` and `Failed` counts.
- Script exits with status `1` when any failures occur.

## Validation Notes

- Example config includes three recipients to meet the project goal.
- Use `--dry-run` during validation in environments where SMTP access is restricted.
