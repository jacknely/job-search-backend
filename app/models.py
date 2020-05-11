import pandas as pd
import requests
import json
from app.job import Job


class Jobs:

    api = "https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev"

    def __init__(self):
        self.jobs = self.download_jobs()

    def __repr__(self):
        return json.dumps(self.jobs.job)

    def download_jobs(self) -> pd.DataFrame:
        """
        downloads a copy of raw job data from aws
        as an df then sets id as index
        :return: df of jobs
        """
        response = requests.get(self.api)
        json_response = response.json()

        return json_response

    def get_job_by_id(self, _id):
        _job = list(filter(lambda x: x["id"] == _id, self.jobs))
        if len(_job) != 1:
            raise Exception(f"ERROR: No jobs with id {_id}")
        return Job(_job[0])


if __name__ == "__main__":
    jobs = Jobs()
    print(jobs)
    #job = jobs.get_job_by_id("0aa482d5e9f803cf")
    #job.update_job(title="A Test")
    #job.send_alert()