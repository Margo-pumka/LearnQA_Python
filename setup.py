import pytest
import requests
class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup_method(self):

        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        self.auth_sid = self.getCookie(response1, "auth_sid")
        self.token = self.getHeader(response1,"x-csrf-token")
        self.getJsonValue(response1, "user_id")


    def test_auth_user(self):
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})
        assert "user_id" in response2.json(), "There is no user_id in the second response"
        user_id_from_check_method = response2.json()["user_id"]
        assert self.user_id_from_auth_method == user_id_from_check_method, \
            "User id from auth method is not equal user id from check method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negativa_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies={"auth_sid": self.auth_sid})
        assert "user_id" in response2.json(), "There is no user_id in the second response"
        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User authorized with condition {condition}"