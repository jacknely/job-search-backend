import pytest
from unittest.mock import patch
import json

from app.job import Job


class TestJob:
    test_data = {"id": "90038429",
                 "title": "Python Developer",
                 "company": "Durlston Partners London Limited",
                 "contract": "Permanent",
                 "age": "Expires in 1 day",
                 "date": "27/04/2022",
                 "location": "EC1, City of London",
                 "link": "https://www.google.com",
                 "agency": "CW Jobs",
                 "summary": "They are... ",
                 "interested": "N",
                 "reviewed": "N",
                 "email": "N"}

    def setup_method(self):
        self.job = Job(self.test_data)

    @patch("app.job.requests.put")
    def test_put_job(self, mock):
        self.job.put_job()

        assert json.loads(mock.call_args.kwargs['data']) == self.test_data

    def test_update_job(self):
        self.job.update_job(title="1")

        assert self.job.job['title'] == "1"

    @patch("app.email_job.Email.send_job_alert")
    def test_send_alert(self, mock):
        self.job.send_alert()

        assert self.job.job['email'] != "N"




