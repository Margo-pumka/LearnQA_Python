from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
class TestUserEdit(BaseCase):
    # REGISTER
    def test_just_created_user(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        firstName = register_data["firstName"]
        password = register_data["password"]
        user_id = self.getJsonValue(response1, "id")

        # LOGIN
        login_data = {
        "email": email,
        "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.getCookie(response2, "auth_sid")
        token = self.getHeader(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName":  new_name})
        Assertions.assert_code_status(response3, 200)

        #GET
        response4= MyRequests.get(f"/user/{user_id}",
                                headers={"x-csrf-token": token},
                                cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of user after edit")

        # EDIT by no auth user
        new_changed_name = "New changed Name"
        response5 = MyRequests.put(f"/user/{user_id}",
                                   data={"firstName": new_name})
        Assertions.assert_code_status(response5, 400)
        assert response5.content.decode("utf-8") == f"Auth token not supplied", \
            f"Unexpected response content {response5.content}"

        # REGISTER and LOGIN other user
        data2 = self.prepare_registration_data()
        response6 = MyRequests.post("/user/", data=data2)
        del data2["username"]
        del data2["firstName"]
        del data2["lastName"]
        response7 = MyRequests.post("/user/login", data=data2)
        auth_sid2 = self.getCookie(response7, "auth_sid")
        token2 = self.getHeader(response7, "x-csrf-token")

        # EDIT by other user
        new_changed_name = "New changed Name"
        response8 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token2},
                                   cookies={"auth_sid": auth_sid2},
                                   data={"firstName": new_changed_name})
        Assertions.assert_code_status(response8, 200)

        # EDIT email without @
        response9 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": "ddddhhttfgfhttryytrty"})
        Assertions.assert_code_status(response9, 400)
        assert response9.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response9.content}"

        # EDIT username with 1 character
        response10 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"username": "h"})
        Assertions.assert_code_status(response10, 400)
        assert response10.content.decode("utf-8") == '{"error":"Too short value for field username"}', \
            f"Unexpected response content {response10.content}"

