# import uiautomator2 as u2
# import time
from curl_cffi import requests
from config import BEARER_TOKEN, ACCOUNT_ID

# from config import BEARER_TOKEN, ACCOUNT_ID, DEVICE_SERIAL
# from instagram_api import report_error


def get_latest_job():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": BEARER_TOKEN,
        "content-type": "application/json;charset=utf-8",
        "origin": "https://app.golike.net",
        "priority": "u=1, i",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "t": "VFZSak1VNXFTVEpPUkdjelRtYzlQUT09",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }

    params = {
        "account_id": ACCOUNT_ID,
    }

    response = requests.get(
        "https://gateway.golike.net/api/advertising/publishers/linkedin/jobs",
        params=params,
        headers=headers,
        impersonate="safari_ios",
    )

    response.encoding = "utf-8"

    if response.status_code != 200:
        print(f"[-] Lỗi khi lấy danh sách job: {response.status_code}")
        print(response.text[:500])  # in 500 ký tự đầu để debug
        return None

    try:
        json_data = response.json()
    except Exception as e:
        print(f"[-] Không thể đọc JSON: {e}")
        return None

    if not json_data.get("success") or not json_data.get("data"):
        print("[-] Không có job mới")
        return None

    job_data = json_data["data"]
    print(f"[+] Job ID: {job_data['id']}")
    print(f"[+] Link Instagram: {job_data['link']}")
    return job_data
