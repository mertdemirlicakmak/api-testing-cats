import requests
import pytest
from pydantic import ValidationError
from app.models import FactModel

BASE_URL = "https://cat-fact.herokuapp.com"


def test_fact_field_types():
    """
    Test to verify the returned Facts' fields exist 
    and their types are as expected.
    """
    # Get cat facts
    response = requests.get(f"{BASE_URL}/facts")
    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']
    facts = response.json()
    
    # Validate each fact against the Pydantic model
    for fact in facts:
        try:
            validated_fact = FactModel(**fact)
        except ValidationError as e:
            pytest.fail(f"Validation error for fact {fact['_id']}: {e}")

def test_fact_randomness():
    """
    Test to verify the 'random fact' feature works. 
    It expects 2 consecutive random facts to be different than each other.
    """
    # Get two random cat facts
    random_fact_1 = requests.get(f"{BASE_URL}/facts/random").json()
    validated_fact_1 = FactModel(**random_fact_1)
    random_fact_2 = requests.get(f"{BASE_URL}/facts/random").json()
    validated_fact_2 = FactModel(**random_fact_2)

    # Check their texts to see if they are different facts
    assert validated_fact_1.text != validated_fact_2.text, "Concussive random facts are same!"
