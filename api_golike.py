from curl_cffi import requests

from config import BEARER_TOKEN, ACCOUNT_ID
from color import RED, YELLOW, GREEN, RESET


def get_header():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": BEARER_TOKEN,
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://app.golike.net",
        "priority": "u=1, i",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "t": "VFZSak1VNXFTVEpPUkd0M1RWRTlQUT09",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }
    return headers


def skip_job(job_data):
    headers = get_header()
    json_data = {
        "account_id": ACCOUNT_ID,
        "ads_id": job_data["id"],
        "object_id": job_data["object_id"],
    }

    response = requests.post(
        "https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs",
        headers=headers,
        json=json_data,
        impersonate="safari_ios",
    )
    response.encoding = "utf-8"
    try:
        result = response.json()
        if result.get("success"):
            print(f"{YELLOW}[+] Skip job thành công: {result.get('message')}{RESET}")
        else:
            print(f"[-] Báo lỗi thất bại: {result}")
    except Exception as e:
        print(f"[-] Lỗi khi đọc JSON từ API: {e}")


def complete_job(job_data):
    headers = get_header()

    json_data = {
        "account_id": ACCOUNT_ID,
        "ads_id": job_data["id"],
    }

    response = requests.post(
        "https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs",
        headers=headers,
        json=json_data,
        impersonate="safari_ios",
    )
    response.encoding = "utf-8"

    try:
        result = response.json()
        if response.status_code == 200 and result.get("success"):
            print(f"{GREEN}[+] Job đã hoàn thành trên GoLike{RESET}")
            return True
        else:
            print(
                f"{RED}[-] Lỗi khi hoàn tất job: {result.get('message', result)}{RESET}"
            )
            return False
    except Exception as e:
        print(f"[-] Lỗi khi đọc JSON từ API hoàn tất: {e}")
        return False
