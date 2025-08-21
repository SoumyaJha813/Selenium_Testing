#Fixtures in pytest are functions that setup test environments before a test runs and cleanups afterwords.
#They help manage test dependencies, setup, teardown, and reusable data across multiple test cases.
#Key features of pytest fixtures.
#reusability -> define once, use in multiple tests
#Automatic Setup & Teardown-> Handles pre-test and post-test actions.
#Scope Control -> Fixtures can run per tests, per class, per modules, or per sessions.
#Dependency injections -> Pass fixtues at test function arguments.


import pytest

@pytest.fixture
def sample_data():
    print("\nSetup: Creating test data")
    data= {"name": "Alice", "age": 30}
    yield data
    print("cleaning up test data")

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print("Test executed successfully")