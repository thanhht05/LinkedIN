import json
import re
import time
from curl_cffi import requests
from color import RED, YELLOW, GREEN, RESET
import re
from get_info_job import get_target_id, get_slug, check_type
from headers import get_header


def click_follow(cookie: str, job_data):
    headers = get_header(cookie, job_data["link"])
    company_slug = get_slug(job_data["link"])

    target_id = get_target_id(cookie, company_slug, job_data["link"])

    json_data = {
        "patch": {
            "$set": {
                "following": True,
            },
        },
    }
    print("Sau 5s sẽ follow")
    for j in range(5):
        print(".", end="", flush=True)
        time.sleep(1)

    if check_type(job_data["link"]) == "COMPANY":
        response = requests.post(
            f"https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:{target_id}",
            headers=headers,
            json=json_data,
        )
    elif check_type(job_data["link"]) == "PROFILE":
        response = requests.post(
            f"https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:{target_id}",
            headers=headers,
            json=json_data,
        )
    print(response.status_code)
    if response.status_code == 200 | response.status_code == 201:
        return True
    else:
        return False
