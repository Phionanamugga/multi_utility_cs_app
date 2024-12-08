def update_status(item, status):
    """Update the status of a reported issue."""
    item["status"] = status
    return item

def filter_by_status(items, status):
    """Filter items by status."""
    return [item for item in items if item["status"] == status]
