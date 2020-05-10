import pytest
from app.job_analysis import JobAnalysis
from unittest.mock import patch, Mock
import pandas as pd
import json


class TestJobAnalysis:

    test_data_json = json.dumps([{"id": "90038429",
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
                                  "email": "N"},
                                 {"id": "9003429",
                                  "title": "Python Developer",
                                  "company": "Durlston Partners London Limited",
                                  "contract": "Permanent",
                                  "age": "Expires in 1 day",
                                  "date": "09/05/2022",
                                  "location": "EC1, City of London",
                                  "link": "https://www.google.com",
                                  "agency": "CW Jobs",
                                  "summary": "They are... ",
                                  "interested": "Y",
                                  "reviewed": "Y",
                                  "email": "N"}
                                 ])

    test_data_pd = pd.read_json(test_data_json)

    def setup_method(self):
        with patch("app.job_analysis.pd.read_json") as read_json_mock:
            read_json_mock.return_value = self.test_data_pd
            self.test_jobs = JobAnalysis('test')

    @patch("app.job_analysis.pd.read_json")
    def test_download_jobs(self, read_json_mock: Mock):
        read_json_mock.return_value = self.test_data_pd
        test_download = self.test_jobs.download_jobs('test')
        print(test_download)

        assert test_download.shape == (2, 12)

    def test_jobs_not_reviewed(self):
        test_not_reviewed = self.test_jobs.weekly_summary()

        assert test_not_reviewed.shape == (1, 12)
