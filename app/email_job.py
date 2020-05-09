import boto3
from botocore.exceptions import ClientError


class Email:

    @classmethod
    def send_mail(cls):
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        SENDER = "Jack Nelson <jackn926@gmail.com>"

        # Replace recipient@example.com with a "To" address. If your account
        # is still in the sandbox, this address must be verified.
        RECIPIENT = "jackn926@live.co.uk"

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        CONFIGURATION_SET = "basic"

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "eu-west-1"

        # The subject line for the email.
        SUBJECT = "New Job Alert"

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("Hi Jack,\r\nr\n"
                     "Check out this new job:\r\n\r\n"
                     "Job: ****r\r\n"
                     "Agency: ****r\r\n"
                     )

        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>New Job Alert @ *****</h1>
          <p>Hi Jack, </p>
          <p>Check out this new job:
          <ul>
          <li>Title: <a href='https://aws.amazon.com/ses/'>*******</a></li>
          <li>Agency: *****</li>
          </ul>
          </p>
        </body>
        </html>
                    """

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=AWS_REGION)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])


if __name__ == "__main__":
    Email.send_mail()