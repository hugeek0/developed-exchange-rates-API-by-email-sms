import smtplib
from email.mime.text import MIMEText
from config import rules


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = rules["mail"]["sender_email"]
    msg["To"] = rules["mail"]["receiver_email"]

    with smtplib.SMTP("smtp.gmail.com", 587) as my_server:
        my_server.starttls()
        my_server.login(rules["mail"]["sender_email"], rules["mail"]["app_password"])
        my_server.sendmail(msg["From"], msg["To"], msg.as_string())
