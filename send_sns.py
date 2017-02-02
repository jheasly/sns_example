import boto3
from sns_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME,\
    PHONE_NUMBER

# https://bradmontgomery.net/blog/sending-sms-messages-amazon-sns-and-python/

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    # If the region doesn't match the region of your keys, you'll get:
    #
    # botocore.errorfactory.InvalidParameterException: An error occurred
    # (InvalidParameter) when calling the Publish operation: Invalid parameter:
    # PhoneNumber Reason: +1XXXXXXXXXX is not valid to publish to
    region_name=REGION_NAME,
)

# Send sms message
client.publish(
    PhoneNumber=PHONE_NUMBER,
    Message="Hello, it's me.",
)
