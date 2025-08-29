import requests
from headers import get_header


def like(cookie, job_data, arg):
    headers = get_header(cookie, job_data["link"])
    params = {
        "action": "execute",
        "queryId": "voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b",
    }

    json_data = {
        "variables": {
            "entity": {
                "reactionType": "LIKE",
            },
            "threadUrn": f"urn:li:{arg}:{job_data["object_id"]}",
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

    if "errors" in data.get("data", {}):
        return False
    return True


def safe_like(cookie, job_data):
    if not like(cookie, job_data, "activity"):
        return like(cookie, job_data, "ugcPost")
    return True
