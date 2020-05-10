import pandas as pd
import numpy as np
import functools
from datetime import datetime, timedelta
from io import StringIO


class JobAnalysis:

    def __init__(self, db_location):
        self.jobs = self.download_jobs(db_location)

    @staticmethod
    def download_jobs(db_location) -> pd.DataFrame:
        """
        downloads a copy of raw job data from aws
        as an df then sets id as index
        :return: df of jobs
        """
        jobs_raw = pd.read_json(db_location, convert_dates=False)
        jobs_raw['date'] = pd.to_datetime(jobs_raw['date'], format='%d/%m/%Y')
        jobs = jobs_raw.set_index('id')

        return jobs

    def weekly_summary(self, jobs=None):
        """
        returns a DataFrame of interested
        jobs for the past week.
        :param jobs: jobs
        :return: filtered jobs
        """
        if jobs is None:
            jobs = self.jobs

        c_1 = jobs.reviewed == "Y"
        c_2 = jobs.email == "N"
        c_3 = jobs.interested == "Y"

        week = datetime.today() - timedelta(days=7)
        c_4 = jobs.date >= week

        jobs_filtered = jobs[self.__conjunction(c_1, c_2, c_3, c_4)]

        return jobs_filtered

    def __conjunction(*conditions):
        return functools.reduce(np.logical_and, conditions)


if __name__ == "__main__":
    db_address = "https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev"
    analysis = JobAnalysis(db_address)
    week_jobs = analysis.weekly_summary()


