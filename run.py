# run.py

import logging

from app import create_app
from config import get_config

app = create_app(get_config())

if __name__ == "__main__":
    app.run(port=app.config.get("PORT"))
