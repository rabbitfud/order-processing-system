import json

def lambda_handler(event, context):
    return {
        "status": "IN_STOCK",
        "available": True,
        "order": event
    }
