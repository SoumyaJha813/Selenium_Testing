import pytest
#use @pytest.mark.usefixtures("setup") to call setup fixtures in all methods in a class
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("fixture Demo0 ")

    def test_fixtureDemo1(self):
        print("fixture Demo1")

    def test_fixtureDemo2(self):
        print("fixture Demo2")

    def test_fixtureDemo3(self):
        print("fixture Demo3")