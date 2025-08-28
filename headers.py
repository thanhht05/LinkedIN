import re
from list_user_agents import windows_chrome_agents
import random


def get_header(cookie: str, url):
    ua = random.choice(windows_chrome_agents)
    csrf = re.findall(r'SESSIONID="([^"]+)"', str(cookie))[0]
    headers = {
        "accept": "application/vnd.linkedin.normalized+json+2.1",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json; charset=UTF-8",
        "csrf-token": csrf,
        "origin": "https://www.linkedin.com",
        "priority": "u=1, i",
        "referer": url,
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "user-agent": ua,
        "x-li-lang": "en_US",
        "x-li-page-instance": "urn:li:page:d_flagship3_company;JsS+biQ4T6ewjQ+LaBQYOQ==",
        "x-li-pem-metadata": "Voyager - Organization - Member=organization-follow",
        "x-li-track": '{"clientVersion":"1.13.38426","mpVersion":"1.13.38426","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
        "x-restli-protocol-version": "2.0.0",
        "cookie": str(cookie),
    }

    return headers
