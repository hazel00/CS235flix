import os
import pytest

from flix_web_app import create_app
from flix_web_app.adapters import memory_repository
from flix_web_app.adapters.memory_repository import MemoryRepository

TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'woodw', 'OneDrive', 'Desktop')