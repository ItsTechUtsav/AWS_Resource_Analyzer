import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


def send_email():
    load_dotenv()

    sender_email = os.getenv("EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    app_password = os.getenv("EMAIL_PASSWORD")

    message = EmailMessage()

    message["Subject"] = "AWS Cost Optimization Report"

    message["From"] = sender_email

    message["To"] = receiver_email

    message.set_content(
        """
Hello,

Today's AWS Cost Optimization Report is attached.

Regards,
AWS Cost Optimizer
"""
    )

    # Attach HTML Report
    with open("reports/report.html", "rb") as file:

        message.add_attachment(
            file.read(),
            maintype="text",
            subtype="html",
            filename="report.html"
        )

    # Send Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)

        smtp.send_message(message)

    print("Email Sent Successfully!")