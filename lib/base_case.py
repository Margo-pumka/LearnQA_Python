import json.decoder
from requests import Response
class BaseCase:
    def getCookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def getHeader(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def getJsonValue(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        return response_as_dict[name]
