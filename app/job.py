from lambda_funcs.cw_jobs.handler import download_jobs as cw_jobs_download_jobs
from lambda_funcs.indeed.handler import download_jobs as indeed_download_jobs
from lambda_funcs.reed.handler import download_jobs as reed_download_jobs

if __name__ == "__main__":
    print(reed_download_jobs())
