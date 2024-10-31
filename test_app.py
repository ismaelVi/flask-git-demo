from app import calculate_age, get_zodiac_sign, days_to_birthday
from datetime import date

import pytest
from app import app

def test_calculate_age():
    assert calculate_age("1990-01-01") == date.today().year - 1990

def test_get_zodiac_sign():
    assert get_zodiac_sign("1990-01-01") == "Capricorn"
    assert get_zodiac_sign("1990-07-01") == "Cancer"

def test_days_to_birthday():
    today = date.today()
    next_birthday = date(today.year, 12, 31)
    if next_birthday < today:
        next_birthday = date(today.year + 1, 12, 31)
    expected_days = (next_birthday - today).days
    assert days_to_birthday("2000-12-31") == expected_days

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Birthday App" in response.data

def test_form_submission(client):
    response = client.post('/', data={
        'name': 'John Doe',
        'dob': '1990-01-01'
    }, follow_redirects=True)
    assert response.status_code == 200
    print(response.data)
    assert b"John Doe" in response.data
    assert b"years old" in response.data
    assert b"with the zodiac sign" in response.data