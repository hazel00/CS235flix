from flask import Flask

import flix_web_app.adapters.repository as repo
from flix_web_app.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')

    if test_config is not None:
        app.config.from_mapping(test_config)

    repo.repo_instance = MemoryRepository()
    populate('flix_web_app/datafiles/users.csv', 'flix_web_app/datafiles/Data1000Movies.csv', repo.repo_instance)

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .logging_in import logging_in
        app.register_blueprint(logging_in.logging_in_blueprint)

    return app
