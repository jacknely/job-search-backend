# flake8: noqa
activate_this = "/home/ubuntu/venv/bin/activate_this.py"
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/job-search-backend/")

from app import create_app

application = create_app("config.DevConfig")
