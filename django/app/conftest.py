from environs import Env
from django.conf import settings

import pytest

env = Env()
env.read_env()

DEFAULT_ENGINE = "django.db.backends.postgresql"

#
# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["default"] = {
#         "ENGINE": env.str("DB_TEST_ENGINE", DEFAULT_ENGINE),
#         "HOST": env.str("DB_TEST_HOST", ""),
#         "NAME": env.str("DB_TEST_NAME", ""),
#         "PORT": env.str("DB_TEST_PORT", ""),
#         "USER": env.str("DB_TEST_USER", ""),
#         "PASSWORD": env.str("DB_TEST_PASSWORD", ""),
#     }
