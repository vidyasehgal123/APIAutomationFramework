import allure
import pytest
import allure_pytest
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

@pytest.mark.smoke
def test_testcase_1():
    assert 1+1==2
    print("hello")
@pytest.mark.smoke
def test_testcase_2():
    print("hello")

@pytest.mark.reg
def test_testcase_3():
    print("hello")

@pytest.mark.skip(reason="Not completed,skip it")
def test_testcase_4():
    print("yello")


