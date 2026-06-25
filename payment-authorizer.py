import json

def lambda_handler(event, context):
    return {
        "status": "PAYMENT_APPROVED",
        "paymentId": "PAY12345",
        "order": event
    }
