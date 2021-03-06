import pytest
from app.job_analysis import JobAnalysis
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
        self.jobs_anal = JobAnalysis(self.test_data_json)

    def test_get_as_pd(self):
        expected = self.jobs_anal.get_as_pd(self.test_data_json)

        assert expected.shape == (2, 12)

    def test_weekly_summary(self):
        expected = self.jobs_anal.weekly_summary()

        assert expected.shape == (1, 12)



