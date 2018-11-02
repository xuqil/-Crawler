import requests
import urllib3
from requests.exceptions import ReadTimeout, HTTPError, RequestException

try:
    urllib3.disable_warnings()
    response = requests.get("https://www.12306.cn", verify=False, timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('TimeOut')
except HTTPError:
    print("error")
except RequestException:
    print("error")
# for key, value in response.cookies.items():
#     print(key + "=" + value)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)
