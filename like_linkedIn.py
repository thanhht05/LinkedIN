import re
import time
import requests
from headers import get_header


def extract_ids_from_file(path="like.html"):
    """Trả về dict chỉ chứa activity[0] và ugcPost[0] từ file"""
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()

    activity = re.findall(r"urn:li:activity:(\d+)", txt)
    ugcPost = re.findall(r"urn:li:ugcPost:(\d+)", txt)

    return {
        "activity": activity[0] if activity else None,
        "ugcPost": ugcPost[0] if ugcPost else None,
    }


def like(cookie, arg, link, data_file="like.html"):
    ids = extract_ids_from_file(data_file)
    object_id = ids.get(arg)
    if not object_id:
        print(f"❌ Không tìm thấy {arg} id trong file {data_file}")
        return False

    headers = get_header(cookie, link)
    params = {
        "action": "execute",
        "queryId": "voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b",
    }

    json_data = {
        "variables": {
            "entity": {"reactionType": "LIKE"},
            "threadUrn": f"urn:li:{arg}:{object_id}",
        },
        "queryId": "voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b",
        "includeWebMetadata": True,
    }

    response = requests.post(
        "https://www.linkedin.com/voyager/api/graphql",
        params=params,
        headers=headers,
        json=json_data,
    )
    data = response.json()

    # Lấy errors từ đúng path
    errors = data.get("data", {}).get("errors") or data.get("errors")

    if errors:
        status = errors[0].get("extensions", {}).get("status")
        message = errors[0].get("message")
        print(
            f"❌ Like {arg}:{object_id} thất bại | Status: {status} | Message: {message}"
        )
        return False

    print(f"✅ Like {arg}:{object_id} thành công.")
    return True


def safe_like(cookie, job_data, data_file="like.html"):
    print("⏳ Sau 5s sẽ like...")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

    # Thử activity trước
    if like(cookie, "activity", job_data["link"], data_file):
        return True

    # Nếu activity fail thì thử ugcPost
    if like(cookie, "ugcPost", job_data["link"], data_file):
        return True

    print("❌ Không like được activity hay ugcPost nào")
    return False
