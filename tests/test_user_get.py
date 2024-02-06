from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
class TestUserGet(BaseCase):
    def test_user_detail_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.getCookie(response1, "auth_sid")
        token = self.getHeader(response1, "x-csrf-token")
        user_id_from_auth_method = self.getJsonValue(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

        # Assertions.assert_json_has_key(response2, "username")
        # Assertions.assert_json_has_key(response2, "email")
        # Assertions.assert_json_has_key(response2, "first_name")
        # Assertions.assert_json_has_key(response2, "last_name")

    def test_get_user_details_auth_as_other_user(self):

        data1 = self.prepare_registration_data()
        response1reg = MyRequests.post("/user/", data=data1)
        del data1["username"]
        del data1["firstName"]
        del data1["lastName"]
        response1auth = MyRequests.post("/user/login", data=data1)
        auth_sid1 = self.getCookie(response1auth, "auth_sid")
        token1 = self.getHeader(response1auth, "x-csrf-token")


        data2 = self.prepare_registration_data()
        response2reg = MyRequests.post("/user/", data=data2)
        del data2["username"]
        del data2["firstName"]
        del data2["lastName"]
        response2auth = MyRequests.post("/user/login", data=data2)
        user_id_from_auth_method2 = self.getJsonValue(response2auth, "user_id")

        response3 = MyRequests.get(f"/user/{user_id_from_auth_method2}",
                                 headers={"x-csrf-token": token1}, cookies={"auth_sid": auth_sid1})
        unexpected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_keys(response3, unexpected_fields)



