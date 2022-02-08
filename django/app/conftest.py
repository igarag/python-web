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

from movies.models import Movie


@pytest.fixture(scope="function")
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie

    return _add_movie
