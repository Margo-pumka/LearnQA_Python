import requests
import pytest
from json import JSONDecodeError
class TestUserAgent:
    agents = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'),
    ]
    @pytest.mark.parametrize('agent', agents)
    def test_user_agent(self, agent):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",headers={'User-Agent': agent})
        try:
            assert 'platform' in response.json(), "There is no \'platform\' in response"
            assert 'browser' in response.json(), "There is no \'browser\' in response"
            assert 'device' in response.json(), "There is no \'device\' in response"
        except JSONDecodeError:
            "Response is not in a JSON format"

        if agent == 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30':
            assert response.json()['platform'] == 'Mobile', "Wrong platform in response for User-Agent 1"
            assert response.json()['browser'] == 'No', "Wrong browser in response for User-Agent 1"
            assert response.json()['device'] == 'Android', "Wrong device in response for User-Agent 1"
        if agent == 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1':
            assert response.json()['platform'] == 'Mobile', "Wrong platform in response for User-Agent 2"
            assert response.json()['browser'] == 'Chrome', "Wrong browser in response for User-Agent 2"
            assert response.json()['device'] == 'iOS', "Wrong device in response for User-Agent 2"
        if agent == 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)':
            assert response.json()['platform'] == 'Googlebot', "Wrong platform in response for User-Agent 3"
            assert response.json()['browser'] == 'Unknown', "Wrong browser in response for User-Agent 3"
            assert response.json()['device'] == 'Unknown', "Wrong device in response for User-Agent 3"
        if agent == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0':
            assert response.json()['platform'] == 'Web', "Wrong platform in response for User-Agent 4"
            assert response.json()['browser'] == 'Chrome', "Wrong browser in response for User-Agent 4"
            assert response.json()['device'] == 'No', "Wrong device in response for User-Agent 4"
        if agent == 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1':
            assert response.json()['platform'] == 'Mobile', "Wrong platform in response for User-Agent 5"
            assert response.json()['browser'] == 'No', "Wrong browser in response for User-Agent 5"
            assert response.json()['device'] == 'iPhone', "Wrong device in response for User-Agent 5"












