import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import random
import string
class TestUserRegister1(BaseCase):


    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        email = "vinkotovexample.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response.content}"

    parameters = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]
    @pytest.mark.parametrize('parameter', parameters)
    def test_create_user_without_required_parameter(self, parameter):
        data = self.prepare_registration_data()
        data.pop(parameter)
        response = MyRequests.post("/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}."
        assert response.content.decode("utf-8") == f"The following required params are missed: {parameter}", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_short_and_long_username(self):
        username1 = ''.join(random.choices(string.ascii_letters, k=1))
        data = self.prepare_registration_data()
        data["username"] = username1
        response = MyRequests.post("/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected response content {response.content}"
        username2 = ''.join(random.choices(string.ascii_letters, k=251))
        data = self.prepare_registration_data()
        data["username"] = username2
        response = MyRequests.post("/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", \
            f"Unexpected response content {response.content}"










