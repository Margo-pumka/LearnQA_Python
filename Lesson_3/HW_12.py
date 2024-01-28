import requests
import datetime
class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        expected_headers = {
            'Date': '',
            'Content-Type': 'application/json',
            'Content-Length': '15',
            'Connection': 'keep-alive',
            'Keep-Alive': 'timeout=10',
            'Server': 'Apache',
            'x-secret-homework-header': 'Some secret value',
            'Cache-Control': 'max-age=0',
            'Expires': ''
        }
        for key, value in expected_headers.items():
            assert key in response.headers, f"There is no header {key} in response"
            if key == 'Date' or key == 'Expires':
                current_time1 = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                    seconds=-2)).strftime('%a, %d %b %Y %H:%M:%S GMT')
                current_time2 = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                    seconds=-1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
                assert (response.headers[key] == current_time1) or (response.headers[key] == current_time2), "Wrong current time"
            else:
                assert response.headers[key] == value, f"Header \'{key}\' has unexpected value \'{value}\'"






