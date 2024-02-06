from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
class TestUserEdit(BaseCase):
    def test_user_2_delete(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response_login = MyRequests.post("/user/login", data=data)
        auth_sid = self.getCookie(response_login, "auth_sid")
        token = self.getHeader(response_login, "x-csrf-token")
        response_delete = MyRequests.delete(f"/user/2", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response_delete, 400)
        assert response_delete.content.decode("utf-8") == 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.', \
            f"Unexpected response content {response_delete.content}"

    def test_new_user_delete(self):
        data2 = self.prepare_registration_data()
        response2_register = MyRequests.post("/user/", data=data2)
        del data2["username"]
        del data2["firstName"]
        del data2["lastName"]
        response2_login = MyRequests.post("/user/login", data=data2)
        auth_sid2 = self.getCookie(response2_login, "auth_sid")
        token2 = self.getHeader(response2_login, "x-csrf-token")
        user_id_from_auth_method2 = self.getJsonValue(response2_login, "user_id")
        response2_delete = MyRequests.delete(f"/user/{user_id_from_auth_method2}", headers={"x-csrf-token": token2}, cookies={"auth_sid": auth_sid2})
        Assertions.assert_code_status(response2_delete, 200)


