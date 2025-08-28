import json
from curl_cffi import requests
from color import YELLOW, RESET, ORANGE

BEARER_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NTYwNDYyMzUsImV4cCI6MTc4NzU4MjIzNSwibmJmIjoxNzU2MDQ2MjM1LCJqdGkiOiI3TkxVeFh6OVdURlEzOGZEIiwic3ViIjozMDYyNjg3LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.wPHoaeNu7uHrPCV8pELsAs0iCwfXJxGFMZAwxSBZGAM"


def get_accounts():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": BEARER_TOKEN,
        "content-type": "application/json;charset=utf-8",
        "origin": "https://app.golike.net",
        "priority": "u=1, i",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "t": "VFZSak1VNVVXVEpPZWxrd1RYYzlQUT09",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    }

    response = requests.get(
        "https://gateway.golike.net/api/linkedin-account",
        headers=headers,
        impersonate="safari_ios",
    )
    data = json.loads(response.text)
    listAcc = data.get("data", [])

    rs = []
    for item in listAcc:
        rs.append({item["id"], item["name"]})

    return rs


l = get_accounts()
print(f"{ORANGE}Dánh sách account{RESET}")
print(l)

ACCOUNT_ID = input(f"{YELLOW}Nhập account muốn làm:{RESET} ")
