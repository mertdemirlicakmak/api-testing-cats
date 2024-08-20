# API testing (Cats API)

This repo contains 2 tests for testing the Cats API.

### Test 1:

| Steps | Description |
| ------- | --- |
| Step 1 | Get cat facts |
| Step 2 | Iterate over the list of facts and verify the types and existense of response fields using Pydantic models |

### Test 2:

| Steps | Description |
| ------- | --- |
| Step 1 | Get 2 random cat facts |
| Step 2 | Validate the facts against the model |
| Step 3 | Compare their texts and verify that they are not same |

## Prerequisites
- Create a virtual environment (Python 3.12)
- Install requirements via pip:
`pip install -r requirements.txt`
- Run tests with: 
`pytest -v`