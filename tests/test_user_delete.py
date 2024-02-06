# from lib.base_case import BaseCase
# from lib.assertions import Assertions
# from lib.my_requests import MyRequests
# class TestUserEdit(BaseCase):
#     def test_user_2_delete(self):
#         data = {
#             "email": "vinkotov@example.com",
#             "password": "1234"
#         }
#         response_login = MyRequests.post("/user/login", data=data)
#         auth_sid = self.getCookie(response_login, "auth_sid")
#         token = self.getHeader(response_login, "x-csrf-token")
#         response_delete = MyRequests.delete(f"/user/2", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
#         Assertions.assert_code_status(response_delete, 200)