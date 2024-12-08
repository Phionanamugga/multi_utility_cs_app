import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body content.
        
    Returns:
        dict: Success or error message.
    """
    try:
        # SMTP server configuration
        smtp_server = current_app.config['SMTP_SERVER']
        smtp_port = current_app.config['SMTP_PORT']
        smtp_user = current_app.config['SMTP_USERNAME']
        smtp_password = current_app.config['SMTP_PASSWORD']
        from_email = current_app.config['SMTP_FROM_EMAIL']

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()

        return {"message": "Email sent successfully."}

    except Exception as e:
        return {"error": f"Failed to send email: {str(e)}"}

def send_account_creation_email(to_email, name):
    """
    Sends a welcome email to the user after account creation.
    
    Args:
        to_email (str): User's email address.
        name (str): User's name.
    """
    subject = "Welcome to Multi-Utility Services"
    body = f"Hello {name},\n\nWelcome to Multi-Utility Services! We are thrilled to have you on board.\n\nBest regards,\nThe Multi-Utility Services Team"
    return send_email(to_email, subject, body)

def send_outage_report_email(to_email, ticket_id, location):
    """
    Sends an email confirmation for a power outage report.
    
    Args:
        to_email (str): User's email address.
        ticket_id (str): Outage report ticket ID.
        location (str): Location of the reported outage.
    """
    subject = "Power Outage Report Confirmation"
    body = f"Hello,\n\nWe have received your power outage report for {location}. Your ticket ID is {ticket_id}. Our team will address this issue promptly.\n\nThank you,\nThe Multi-Utility Services Team"
    return send_email(to_email, subject, body)

def send_water_issue_email(to_email, ticket_id, issue_type):
    """
    Sends an email confirmation for a water supply issue report.
    
    Args:
        to_email (str): User's email address.
        ticket_id (str): Water supply issue report ticket ID.
        issue_type (str): Type of issue reported (e.g., "no supply", "leak").
    """
    subject = "Water Supply Issue Report Confirmation"
    body = f"Hello,\n\nWe have received your water supply issue report ({issue_type}). Your ticket ID is {ticket_id}. Our team will address this issue promptly.\n\nThank you,\nThe Multi-Utility Services Team"
    return send_email(to_email, subject, body)

def send_ferry_missed_trip_email(to_email, ticket_id, trip_time):
    """
    Sends an email confirmation for a missed ferry trip report.
    
    Args:
        to_email (str): User's email address.
        ticket_id (str): Missed trip report ticket ID.
        trip_time (str): Time of the missed ferry trip.
    """
    subject = "Missed Ferry Trip Report Confirmation"
    body = f"Hello,\n\nWe have received your report for the missed ferry trip at {trip_time}. Your ticket ID is {ticket_id}. Our team will investigate this issue.\n\nThank you,\nThe Multi-Utility Services Team"
    return send_email(to_email, subject, body)
