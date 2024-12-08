import uuid
from datetime import datetime

def generate_ticket_id():
    """Generate a unique ticket ID."""
    return str(uuid.uuid4())

def format_ticket_response(ticket_id, service_type):
    """Create a user-friendly ticket response message."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "ticket_id": ticket_id,
        "message": f"Your {service_type} issue has been logged successfully.",
        "timestamp": timestamp,
    }
