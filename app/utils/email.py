from fastapi import BackgroundTasks

def send_email(background_tasks: BackgroundTasks, email_to: str, subject: str, body: str):
    background_tasks.add_task(fake_send_email, email_to, subject, body)

def fake_send_email(email_to: str, subject: str, body: str):
    print(f"Sending email to {email_to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")