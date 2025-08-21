#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#method name should make sense
# - k <testcase> stands for method name execution, -s logs the output, -v stands for more info
#you can run specific file py.test <filename>
# Smoke testcase or regression testcases - how to run only those - tag those testcases #py.test  -s -v -m smoke
#you can mark tests with @pytest.mark.smoke - and run with -m smoke option
#how to skip 1 testcase - @pytest.mark.skip
#how to skip only the result/report but you want the testcase to be executed - @pytest.mark.xfail
#fixtures - are used as setup and teardown methods for test cases - conftest file when you want to run few prerequisite like setting the environment - @pytest.fixture() pass the method in another method to call the fixture
#Example: Launching a browser, Logging into application, setting up test data(loading data), closing the browser after test execution
#conftest file is used to keep the fixtures at one place and make it available to all test casaes
#fixtures - yeild - acts as teardown
#datadriven and parameterization can be done with return statement in tuple format give params in fixture
#fixtures scope - when you define fixture scope to class only, it will run once before class is initiated in beginning and once in end
import pytest


@pytest.mark.smoker
def test_firstprogramprint(setup):
    print("Hello")

@pytest.mark.skip
def test_secondprogramgreeting():
    msg = "Hello" #operation
    assert msg == "Hi", "Test failed cause string don't match"

@pytest.mark.xfail
def test_thirdprogrammultiply():
    a = 4
    b = 3
    assert (a*2) == b, "Not matching"

def test_fixturesDemo(setup):
    print("I'll be executing steps in fixtureDemo method")

#Parameterizing test with multiple data sets using Fixtures
def test_crossBrowser(setup, crossBrowser):
    print(crossBrowser[1])
