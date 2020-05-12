![Python app](https://github.com/jacknely/job-search-backend/workflows/Python%20application/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# :office: Job Search: SES & BackEnd
Python application that reads jobs from a AWS DynamoDB that were scraped using [Job Scraper](https://github.com/jacknely/job_scrape_lambda). Various emails
are sent using AWS SES based on events. Flask framework installation for future expansion.

## Requirement
Install from requirements.txt:
- Python 3.8
- Boto3
- Pandas
- Flask
