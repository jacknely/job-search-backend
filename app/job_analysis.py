import functools
import json
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from app.job import Job
from app.jobs import Jobs


class JobAnalysis:

    def __init__(self, jobs_json):
        self.jobs = self.get_as_pd(jobs_json)

    @staticmethod
    def get_as_pd(_json) -> pd.DataFrame:
        """
        downloads a copy of raw job data from aws
        as an df then sets id as index
        :return: df of jobs
        """
        jobs_raw = pd.read_json(_json, convert_dates=False)
        jobs_raw["date"] = pd.to_datetime(jobs_raw["date"], format="%d/%m/%Y")
        jobs_df = jobs_raw.set_index("id")

        return jobs_df

    def weekly_summary(self, jobs_data=None):
        """
        returns a DataFrame of interested
        jobs for the past week.
        :param jobs_data: jobs
        :return: filtered jobs
        """
        if jobs_data is None:
            jobs_data = self.jobs

        c_1 = jobs_data.reviewed == "Y"
        c_2 = jobs_data.email == "N"
        c_3 = jobs_data.interested == "Y"

        week = datetime.today() - timedelta(days=7)
        c_4 = jobs_data.date >= week

        jobs_filtered = jobs_data[self.__conjunction(c_1, c_2, c_3, c_4)]

        return jobs_filtered

    def __conjunction(*conditions):
        return functools.reduce(np.logical_and, conditions)

    def job_alert(self):
        job = Job("id")
        job.send_alert()


if __name__ == "__main__":
    jobs = Jobs()
    jobs_as_json = json.dumps(jobs.jobs)
    analysis = JobAnalysis(jobs_as_json)
    print(analysis.weekly_summary())

