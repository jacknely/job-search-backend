import pandas as pd


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
        jobs_import = pd.read_json(db_location)
        jobs = jobs_import.set_index('id')
        return jobs

    def get_jobs_not_reviewed(self) -> pd.DataFrame:
        """
        returns a df of jobs that have no been
        reviewed in self.jobs
        :return: df of jobs not reviewed
        or ValueError if empty
        """
        jobs_not_reviewed = self.jobs[(self.jobs.reviewed == "N")]
        if jobs_not_reviewed.empty:
            raise ValueError("No jobs to be analysed")
        return jobs_not_reviewed


if __name__ == "__main__":
    analysis = JobAnalysis('https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev')
    print(analysis.get_jobs_not_reviewed())
