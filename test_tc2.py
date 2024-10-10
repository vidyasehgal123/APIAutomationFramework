import allure
import pytest
import allure_pytest
import requests
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")


def test_get_single_URL_by_id():
   url="https://restful-booker.herokuapp.com/booking/1"
   responseData = requests.get(url)
   print(responseData.text)
   print(responseData.headers)
   print(responseData.json())
   assert responseData.status_code==200

@allure.title("Negative Test Case")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")

def test_negative_testing():
   url = "https://restful-booker.herokuapp.com/booking/-1"
   response_Data = requests.get(url)
   assert response_Data.status_code == 404


