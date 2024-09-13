from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from backend.app.core.config import Settings

def send_email_with_report(recipient_email: str, report_url: str) -> str:
    # HUMAN ASSISTANCE NEEDED
    # The following implementation is a basic structure and may need adjustments
    # based on the specific SMTP server configuration and error handling requirements.
    
    settings = Settings()
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_SENDER
    msg['To'] = recipient_email
    msg['Subject'] = "GitHub Repository Scanner Report"

    # Add body text
    body = f"Please find attached the GitHub Repository Scanner report.\n\nReport URL: {report_url}"
    msg.attach(MIMEText(body, 'plain'))

    # Add the report URL as an attachment
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(report_url.encode())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f"attachment; filename=report_url.txt")
    msg.attach(attachment)

    try:
        # Connect to the SMTP server
        with SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
            
            # Send the email
            server.send_message(msg)
        
        return "Email sent successfully"
    except Exception as e:
        # HUMAN ASSISTANCE NEEDED
        # Implement proper error handling and logging here
        return f"Failed to send email: {str(e)}"
