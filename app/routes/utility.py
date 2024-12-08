from datetime import datetime
import uuid
from multi_utility_cs_app.services.email_service import (
    send_outage_report_email, send_water_issue_email, send_ferry_missed_trip_email
)
from multi_utility_cs_app.services.phone_service import (
    send_outage_report_sms, send_water_issue_sms, send_ferry_missed_trip_sms
)

# Example usage after creating a ticket for a power outage
send_outage_report_sms(user.phone, ticket_id, location)


# Example usage after creating a ticket for a power outage
send_outage_report_email(user.email, ticket_id, location)


# Simulated database for simplicity
reports_db = {
    "power_outages": [],
    "water_issues": [],
    "ferry_missed_trips": []
}


def generate_ticket_id():
    """Generates a unique ticket ID."""
    return str(uuid.uuid4())



# --------------------------
# User-Facing Functions
# --------------------------

def report_power_outage(location=None, account_id=None):
    """
    Allows a user to report a power outage.
    Args:
        location (str): User's location.
        account_id (str): User's account ID.
    Returns:
        dict: Confirmation message with ticket ID.
    """
    if not location and not account_id:
        return {"error": "Location or account ID is required to report an outage."}
    
    ticket_id = generate_ticket_id()
    report = {
        "ticket_id": ticket_id,
        "type": "Power Outage",
        "location": location,
        "account_id": account_id,
        "status": "Pending",
        "timestamp": datetime.now().isoformat()
    }
    reports_db["power_outages"].append(report)
    return {"message": "Power outage reported successfully.", "ticket_id": ticket_id}


def report_water_issue(location, issue_type):
    """
    Allows a user to report water supply issues.
    Args:
        location (str): User's location.
        issue_type (str): Type of issue (e.g., "no supply", "leak").
    Returns:
        dict: Confirmation message with ticket ID.
    """
    if not location or not issue_type:
        return {"error": "Both location and issue type are required to report a water issue."}
    
    ticket_id = generate_ticket_id()
    report = {
        "ticket_id": ticket_id,
        "type": "Water Issue",
        "location": location,
        "issue_type": issue_type,
        "status": "Pending",
        "timestamp": datetime.now().isoformat()
    }
    reports_db["water_issues"].append(report)
    return {"message": "Water issue reported successfully.", "ticket_id": ticket_id}


def report_ferry_missed_trip(location, trip_time):
    """
    Allows a user to report a missed ferry trip.
    Args:
        location (str): Ferry terminal or location.
        trip_time (str): Time of the missed trip.
    Returns:
        dict: Confirmation message with ticket ID.
    """
    if not location or not trip_time:
        return {"error": "Both location and trip time are required to report a missed trip."}
    
    ticket_id = generate_ticket_id()
    report = {
        "ticket_id": ticket_id,
        "type": "Missed Ferry Trip",
        "location": location,
        "trip_time": trip_time,
        "status": "Pending",
        "timestamp": datetime.now().isoformat()
    }
    reports_db["ferry_missed_trips"].append(report)
    return {"message": "Missed ferry trip reported successfully.", "ticket_id": ticket_id}


# --------------------------
# Admin-Facing Functions
# --------------------------

def get_all_reports(report_type):
    """
    Retrieves all reports of a given type.
    Args:
        report_type (str): The type of report to retrieve (e.g., "power_outages").
    Returns:
        list: List of reports.
    """
    return reports_db.get(report_type, [])


def update_report_status(ticket_id, report_type, new_status):
    """
    Updates the status of a specific report.
    Args:
        ticket_id (str): The ticket ID of the report.
        report_type (str): The type of report (e.g., "power_outages").
        new_status (str): The new status (e.g., "Resolved").
    Returns:
        dict: Status update result.
    """
    reports = reports_db.get(report_type, [])
    for report in reports:
        if report["ticket_id"] == ticket_id:
            report["status"] = new_status
            return {"message": "Report status updated successfully.", "ticket_id": ticket_id}
    return {"error": "Report not found."}


# --------------------------
# Example Usage
# --------------------------

if __name__ == "__main__":
    # User reports
    print(report_power_outage(location="123 Main Street"))
    print(report_water_issue(location="456 Elm Street", issue_type="Leak"))
    print(report_ferry_missed_trip(location="Harbor Terminal A", trip_time="2024-12-06 10:00 AM"))

    # Admin views all reports
    print("\nAdmin: View All Power Outages")
    print(get_all_reports("power_outages"))

    print("\nAdmin: View All Water Issues")
    print(get_all_reports("water_issues"))

    # Admin updates report status
    print("\nAdmin: Update Status")
    power_reports = get_all_reports("power_outages")
    if power_reports:
        ticket_id_to_update = power_reports[0]["ticket_id"]
        print(update_report_status(ticket_id=ticket_id_to_update, report_type="power_outages", new_status="Resolved"))
