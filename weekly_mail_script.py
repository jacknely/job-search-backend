"""
this script is ran by crontab
on ubuntu 18.04 to send a weekly
email on interested jobs
"""

from app.job_analysis import JobAnalysis
from app.email_job import Email

db_address = "https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev"
analysis = JobAnalysis(db_address)
week_jobs = analysis.weekly_summary()
jobs_dict = week_jobs.to_dict(orient='records')

mail = Email()
mail.send_weekly_mail(jobs_dict)
