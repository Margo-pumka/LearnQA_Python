import requests
class TestCookies:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))
        assert response.cookies, "There is no cookies in the response"
        assert "HomeWork" in response.cookies, "There is no field \'HomeWork\' in the cookies"
        assert response.cookies["HomeWork"] == "hw_value", f"Value of the field \'HomeWork\' is not \'hw_value\'"



