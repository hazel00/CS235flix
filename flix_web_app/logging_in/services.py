from werkzeug.security import generate_password_hash, check_password_hash

from flix_web_app.adapters.repository import AbstractRepository
from flix_web_app.domainmodel.user import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class ValidationException(Exception):
    pass


def add_user(username: str, password: str, repo: AbstractRepository):
    user = repo.get_user(username.lower())
    if user is not None:
        raise NameNotUniqueException

    hashed_password = generate_password_hash(password)

    user = User(username, hashed_password)
    repo.add_user(user)


def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username.lower())
    if user is None:
        raise UnknownUserException

    return user


def validate_user(username: str, password: str, repo: AbstractRepository):
    validated = False

    user = repo.get_user(username.lower())
    if user is not None:
        validated = check_password_hash(user.password, password)
    if not validated:
        raise ValidationException