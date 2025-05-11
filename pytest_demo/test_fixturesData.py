import pytest
#Scenario - 1. you only want setup/teardown effect (no return value) - no need to pass fixture to method
#Scenario - 2. you need to use the fixture's return (eg. data or browser instance) -  need to pass fixture to method
@pytest.mark.usefixtures("dataLoad")
class TestExample:
#passing fixture to method as you need the fixture to return the list data.
    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])