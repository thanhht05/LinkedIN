import re
import requests
from headers import get_header


def check_type(url):
    if "linkedin.com/company/" in url:
        return "COMPANY"
    elif "linkedin.com/in/" in url:
        return "PROFILE"
    elif "linkedin.com/posts" in url:
        return "POST"


def get_query_id(cookie: str, url):
    headers = get_header(cookie, url)
    html = requests.get(url, headers=headers).text
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)

    type_url = check_type(url)
    match = None

    if type_url == "COMPANY":
        match = re.search(r"voyagerOrganizationDashCompanies\.[a-f0-9]+", html)
    elif type_url == "PROFILE":
        match = re.search(r"voyagerIdentityDashProfiles\.[a-f0-9]+", html)

    if match:
        return match.group(0)
    return None


def get_target_id(cookie: str, slug: str, url):
    type_url = check_type(url)
    query_id = get_query_id(cookie, url)
    if not query_id:
        return False

    headers = get_header(cookie, url)
    with open("output.html", "r", encoding="utf-8") as f:
        data = f.read()
    if type_url == "COMPANY":
        response = requests.get(
            f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(universalName:{slug})&queryId={query_id}",
            headers=headers,
        )
        matches = re.findall(r"fsd_company:(\d+)", data)
        if matches:
            return matches[0]

    elif type_url == "PROFILE":
        response = requests.get(
            f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(vanityName:{slug})&queryId={query_id}",
            headers=headers,
        )

        matches = re.findall(
            r"targetInviteeResolutionResult&quot;:&quot;urn:li:([^&]+)", data
        )
        if matches:
            return matches[0].split(":")[1]

    return False
