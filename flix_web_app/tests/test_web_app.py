import pytest

from flask import session


def test_register_and_login(run_web_app):
    response_code = run_web_app.get('/logging_in/register').status_code
    assert response_code == 200
    response = run_web_app.post('/logging_in/register', data={'username': 'Hazel', 'password': 'Hazel12345'})
    assert response.headers['Location'] == 'http://localhost/logging_in/login'
    response = run_web_app.post(
        '/logging_in/login',
        data={'username': 'Hazel', 'password': 'Hazel12345'}
    )
    assert response.headers['Location'] == 'http://localhost/'
    response_code = run_web_app.get('/logging_in/login').status_code
    assert response_code == 200
    with run_web_app:
        run_web_app.get('/')
        assert session['username'] == 'hazel'
    with run_web_app:
        run_web_app.get('/logging_in/logout')
        assert 'user_id' not in session


@pytest.mark.parametrize(('username', 'password', 'message'),(
                         ("","", b'Required field'),
                         ("hahaha", "", b'Required field'),
                         ("he","test1234", b'Username must be longer than 5 characters'),
                         ("richard", "jdfjkj33", b'Username already in use, please try again'),
                         ("jfngjfnd", "rr", b'Password must be at least 6 characters, and contain at least one digit')))
def test_invalid_register(run_web_app, username, password, message):
    response = run_web_app.post('/logging_in/register', data={'username': username, 'password': password})
    assert message in response.data


def test_movies_with_x(run_web_app):
    response = run_web_app.post('/search', data={'selection': 'Title', 'search': 'Split'})
    assert b'Split' in response.data
    response = run_web_app.post('/search', data={'selection': 'Actor', 'search': 'Jai Courtney'})
    assert b'Divergent' in response.data
    assert b'Man Down' in response.data
    assert b'Terminator Genisys' in response.data
    assert b'The Exception' in response.data
    response = run_web_app.post('/search', data={'selection': 'Genre', 'search': 'Animation'})
    assert b'Angry Birds' in response.data
    assert b'Ballerina' in response.data
    assert b'Beowulf' in response.data
    response = run_web_app.post('/search', data={'selection': 'Director', 'search': 'M. Night Shyamalan'})
    assert b'After Earth' in response.data
    assert b'Lady in the Water' in response.data
    assert b'Split' in response.data

