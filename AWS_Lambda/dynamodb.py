import boto3
import json
from datetime import datetime

def generate_custom_json(user_text, user_email_text, creation_date_text, event_date_text, original_text, summary_text, keywords_text, url_text):
    custom_json = {
        "creationdate": creation_date_text,
        "user": user_text,
        "useremail": user_email_text,
        "eventdate": event_date_text,
        "originaltext": original_text,
        "summary": summary_text,
        "keywords": keywords_text,
        "url": url_text
    }
    return custom_json
    
def send_custom_json_to_dynamodb(custom_json):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'dynamodbforhack'

    table = dynamodb.Table(table_name)
    response = table.put_item(Item=custom_json)

    return response

def lambda_handler(event, context):
    # Extract JSON information
    creation_date_text = str(datetime.now())
    user_text = event['queryStringParameters']['user_text']
    user_email_text = event['queryStringParameters']['user_email_text']
    original_text = event['queryStringParameters']['original_text']
    url_text = event['queryStringParameters']['url_text']
    event_date_text = '2024/03/19 9:10AM'
    keywords_text = 'Term Test 2, Tuesday, March 19, 2024, 9:10 AM, 10:50 AM, EX 100, Exam Centre, 9 AM, Type D, Calculator, Non-Programmable'
    summary_text = 'Term Test 2 is on March 19 at 9:10-10:50AM in EX 100, Type D exam, allowing non-programmable calculator.'
    
    custom_json = generate_custom_json(user_text, user_email_text, creation_date_text, event_date_text, original_text, summary_text, keywords_text, url_text)

    try:
        dynamodb_response = send_custom_json_to_dynamodb(custom_json)
        print("Item added successfully:", dynamodb_response)
    except Exception as e:
        print("Error adding item to DynamoDB:", str(e))

    return {
        "statusCode": 200,
        "body": json.dumps("Custom JSON sent to DynamoDB")
    }

