import json


def hello(event, context):
    body = {
        "message": "Updated!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
