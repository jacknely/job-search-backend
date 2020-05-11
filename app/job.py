import json
from datetime import datetime

import requests

from app.email_job import Email


class Job:
    """
    class representation of an individual job
    """

    api = "https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev"

    def __init__(self, job: dict):
        self.job = job

    def __repr__(self) -> str:
        return str(self.job)

    def put_job(self) -> requests.Response:
        """
        put request to api with current job object
        :return: Response
        """
        try:
            response = requests.put(self.api, data=json.dumps(self.job))
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return response

    def update_job(self, **kwargs) -> dict:
        """
        updates job object with given
        key, value's
        :param kwargs: items to update
        :return: updated job dict
        """
        for k, v in kwargs.items():
            self.job[k] = v

        return self.job

    def send_alert(self) -> requests.Response:
        """
        sends an email and updates
        api from current job object
        :return: response object
        """
        email = Email()
        email.send_job_alert(self.job)
        timestamp = datetime.timestamp(datetime.now())
        self.update_job(email=str(timestamp))
        response = self.put_job()
        if response.status_code == 200:
            print("message sent")
        else:
            raise Exception("Error job not updated")

        return response
