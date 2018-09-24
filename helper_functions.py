import os
import logging

production_url = "https://freegracealliance-backend.appspot.com"
development_url = "http://localhost:8080"


def get_url():
    if is_development():
        return development_url
    else:
        return production_url


def is_development():
    return os.environ.get("SERVER_SOFTWARE").startswith("Development")


