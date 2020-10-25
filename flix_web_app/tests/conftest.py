import pytest

from flix_web_app import create_app
from flix_web_app.adapters import memory_repository
from flix_web_app.adapters.memory_repository import MemoryRepository


@pytest.fixture
def populated_repo():
    repo = MemoryRepository()
    memory_repository.populate('flix_web_app/datafiles/users.csv', 'flix_web_app/datafiles/Data1000Movies.csv', repo)
    return repo


@pytest.fixture
def run_web_app():
    current_app = create_app({'TESTING': True, "WTF_CSRF_ENABLED": False})
    return current_app.test_client()



