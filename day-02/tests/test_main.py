from app.services.sample_service import greet

def test_greet():
    assert greet('Usman') == 'Hello, Usman'
