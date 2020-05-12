import pytest

from app.jobs import Jobs

from unittest.mock import patch


class TestJobs:

    test_data_json = [{"id": "90038429",
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
                                 ]

    def setup_method(self):
        with patch('app.jobs.requests.get') as mock:
            mock.return_value.json.return_value = self.test_data_json
            self.jobs = Jobs()

    @patch('app.jobs.requests.get')
    def test_download_jobs(self, mock):
        mock.return_value.json.return_value = self.test_data_json
        expected = self.jobs.download_jobs()

        assert expected == self.test_data_json

    def test_get_job_by_id(self):
        expected = self.jobs.get_job_by_id("90038429")

        assert expected.job['id'] == "90038429"
