
 

import json
import pytest
from dotenv import load_dotenv

from users.models import User
from app import create_app
from app import db as _db
from pytest_factoryboy import register
from tests.factories import UserFactory


register(UserFactory)


@pytest.fixture(scope="session")
def app():
    load_dotenv(".testenv")
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()