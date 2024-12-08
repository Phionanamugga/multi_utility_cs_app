import requests
from flask import current_app

def send_sms(to_phone, message):
    """
    Sends an SMS to the specified phone number.
    
    Args:
        to_phone (str): Recipient's phone number in international format (e.g., +1234567890).
        message (str): SMS content.

    Returns:
        dict: Success or error message.
    """
    try:
        # SMS API configuration
        sms_api_url = current_app.config['SMS_API_URL']
        sms_api_key = current_app.config['SMS_API_KEY']
        sender_id = current_app.config['SMS_SENDER_ID']

        # Payload for the SMS API
        payload = {
            'to': to_phone,
            'message': message,
            'sender': sender_id,
            'api_key': sms_api_key
        }

        # Make the API request
        response = requests.post(sms_api_url, data=payload)
        response_data = response.json()

        if response.status_code == 200 and response_data.get('status') == 'success':
            return {"message": "SMS sent successfully."}
        else:
            return {"error": f"Failed to send SMS: {response_data.get('error', 'Unknown error')}"}

    except Exception as e:
        return {"error": f"Error occurred while sending SMS: {str(e)}"}

def send_account_creation_sms(to_phone, name):
    """
    Sends a welcome SMS to the user after account creation.
    
    Args:
        to_phone (str): User's phone number.
        name (str): User's name.
    """
    message = f"Hello {name}, welcome to Multi-Utility Services! We're excited to serve you."
    return send_sms(to_phone, message)

def send_outage_report_sms(to_phone, ticket_id, location):
    """
    Sends an SMS confirmation for a power outage report.
    
    Args:
        to_phone (str): User's phone number.
        ticket_id (str): Outage report ticket ID.
        location (str): Location of the reported outage.
    """
    message = f"Power outage reported for {location}. Ticket ID: {ticket_id}. We will address this promptly."
    return send_sms(to_phone, message)

def send_water_issue_sms(to_phone, ticket_id, issue_type):
    """
    Sends an SMS confirmation for a water supply issue report.
    
    Args:
        to_phone (str): User's phone number.
        ticket_id (str): Water supply issue report ticket ID.
        issue_type (str): Type of issue reported (e.g., "no supply", "leak").
    """
    message = f"Water issue reported ({issue_type}). Ticket ID: {ticket_id}. Our team is on it."
    return send_sms(to_phone, message)

def send_ferry_missed_trip_sms(to_phone, ticket_id, trip_time):
    """
    Sends an SMS confirmation for a missed ferry trip report.
    
    Args:
        to_phone (str): User's phone number.
        ticket_id (str): Missed trip report ticket ID.
        trip_time (str): Time of the missed ferry trip.
    """
    message = f"Missed ferry trip at {trip_time} reported. Ticket ID: {ticket_id}. We will investigate this issue."
    return send_sms(to_phone, message)
