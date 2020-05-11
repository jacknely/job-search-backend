from pathlib import Path

import boto3
from botocore.exceptions import ClientError
from jinja2 import Environment, FileSystemLoader


class Email:
    def send_weekly_mail(self, job_dict):
        env = Environment(
            loader=FileSystemLoader(
                "%s/templates/" % Path(__file__).parent.parent
            )
        )

        template = env.get_template("weekly_email.html")
        output = template.render(jobs=job_dict)
        self.send_mail(output)

    def send_job_alert(self, job):
        env = Environment(
            loader=FileSystemLoader(
                "%s/templates/" % Path(__file__).parent.parent
            )
        )

        template = env.get_template("alert_email.html")
        output = template.render(job=job)
        self.send_mail(output)

    @classmethod
    def send_mail(cls, content):
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
        BODY_TEXT = "Cannot load mail without html"

        # The HTML body of the email.
        BODY_HTML = content

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client("ses", region_name=AWS_REGION)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={"ToAddresses": [RECIPIENT,],},
                Message={
                    "Body": {
                        "Html": {"Charset": CHARSET, "Data": BODY_HTML,},
                        "Text": {"Charset": CHARSET, "Data": BODY_TEXT,},
                    },
                    "Subject": {"Charset": CHARSET, "Data": SUBJECT,},
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            print("Email sent! Message ID:"),
            print(response["MessageId"])


if __name__ == "__main__":
    Email.send_mail("<html><body>I am a test mail</body></html>")
