import requests
import json
from app.email_job import Email

from datetime import datetime


class Job:

    api = "https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev"

    def __init__(self, job):
        self.job = job

    def __repr__(self):
        return str(self.job)

    def put_job(self):
        try:
            response = requests.put(self.api, data=json.dumps(self.job))
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return response

    def update_job(self, **kwargs):
        for k, v in kwargs.items():
            self.job[k] = v

        return self.job

    def send_alert(self):
        email = Email()
        email.send_job_alert(self.job)
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.update_job(email=str(timestamp))
        self.put_job()
        print("message sent")


