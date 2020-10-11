from flask import Flask

import flix_web_app.adapters.repository as repo
from flix_web_app.adapters.memory_repository import MemoryRepository, populate


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')

    repo.repo_instance = MemoryRepository()
    populate('flix_web_app/datafiles/Data1000Movies.csv', repo.repo_instance)

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

    return app
