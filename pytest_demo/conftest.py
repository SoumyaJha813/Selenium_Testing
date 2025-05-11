import pytest


#when you want to run only once as prerequisite and once at last give scope = "class"- @pytest.fixture(scope="class")
#scope="module": The fixture runs once per file (module).
#You could also use scope="session" to share it across multiple files (rarely needed unless you're running large test suites).
@pytest.fixture(scope="class")
def setup():
    print("I'll be executing first")
    yield
    print("I'll be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["soumya", "jha", "riya", "bharadwaj"]

#you want to run the test in multiple browser, i need to run the testcase multiple time and pick the data
@pytest.fixture(params=[("chrome", "soumya", "jha"), ("Firefox", "riya", "bharadwaj"), ("IE", "SS")])
def crossBrowser(request):
    return (request.param)