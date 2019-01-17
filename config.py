import os
import logging


def is_development():
    return os.environ.get("SERVER_SOFTWARE").startswith("Development")


