import json


def hello(event, context):
    body = {
        "message": "Updated haha!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
