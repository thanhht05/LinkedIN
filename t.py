import json
import re
import requests
from headers import get_header
from get_info_job import check_type, get_query_id


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
        )  # thêm dấu - nếu cần
        if matches:
            return matches[0].split(":")[1]

    return False


cookie = 'lms_ads=AQHtJW9t--tQ0AAAAZjvMuXIh10yIiOsIx3R4Th2BJFyNsk6qLxBh2fhIc7ONgIcL7BDaja-BKsHl0k6iN2JDQ0ZI0I4-4RV;_guid=9bba59e0-06cb-44c8-8989-750e0f8d18b4;bcookie="v=2&ec2fdc03-442b-4409-88e4-fe2280c77908";__cf_bm=6dpkJLHMSJlEB5EM1FAQv8JYLmFf3DYQ4EwPzwU0pLo-1756437988-1.0.1.1-bEJF4ZvxRZ1fya02I1vwv.0lwtjfsMdahFtcG2FisXk_9baPFi9DS9JpoPzawx3vkGknm_0PlMeONM4yVHiCC6S4X_BavIeoytrvvFuzuYs;_gcl_au=1.1.974568131.1756359751;g_state={"i_l":0};lms_analytics=AQHtJW9t--tQ0AAAAZjvMuXIh10yIiOsIx3R4Th2BJFyNsk6qLxBh2fhIc7ONgIcL7BDaja-BKsHl0k6iN2JDQ0ZI0I4-4RV;AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1;fptctx2=taBcrIH61PuCVH7eNCyH0LNKRXFdWqLJ6b8ywJyet7UtulUkUoP92bPVN3ws6Yo4lis26nXYyOqloaLLTi6hH6v1RQSSZiFOSTPYnu53v6VW%252bAd%252bjehsX%252b6qocfC%252fb2MXd11OYIvjBjJLevuTUMoNS00hXE7BIWjQMmB8En6bmsjNhLfsFcIGV18j8%252bCaL9N5MkiXJHhkLqXhJIcFzjWYm1%252f%252fp4RIg0eoJtVg1OxP7jqHYzPapH8Ua4I8ZdTYuVG%252fHsy1%252b8ew6d7UNtZzwMvLne5jDWnEzGUVhSlgcLyVmWxL6sJAv8KarqICWG8s7TRSsQ5xqLjddMFQvjwRT2d1v6HkKQf3qPwzUdYXyB7WkwM8CCiaUmaFkdmieTI4wag0RG4HyHC4Xau80KMa9xaDw%253d%253d;li_at=AQEDAUf9ZWADsiAjAAABmO8y0joAAAGZEz9WOk0AJbc8rF-d7cG6K2HHD5uEByrfq73OHpbPbdqo5ie7wUrrBxYDvjIquT8U3s_kT-fmT0Z2LdIzV3BrcA4neeH9FePZTVVt3R2o9bCnxrQ_foH4Yvil;lang=v=2&lang=en-us;lidc="b=OB96:s=O:r=O:a=O:p=O:g=3818:u=57:x=1:i=1756438159:t=1756522977:v=2:sig=AQH4bqdzUIg_ZtHYxXgwkz0_twH2oiFl";aam_uuid=06176110973161480230860678494130966861;AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20329%7CMCMID%7C06026700597502077400810245217340646022%7CMCAAMLH-1757037827%7C3%7CMCAAMB-1757037827%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756440227s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1845589424;AnalyticsSyncHistory=AQJvbq-Q4AEVSwAAAZjvMuQ8eIBxp0wZeWC_xumiIAkrfeptIcHSd3TuehBnQiPRqqiTG3zihhSQF-QDLIeusQ;bscookie="v=1&2025082805421287b76e56-449f-4d31-8488-d719f84c2fb0AQFifnzubDdYDZkFG1FApClYgzKwr1y6";dfpfpt=13b8353c7ad04fffa325a72a08f85b3b;JSESSIONID="ajax:0124919465924536625";li_rm=AQFBA5n2RM_C1QAAAZjvMrNwCnzL4ghposhb5HXOxNHycQMrnjObigaint7S3pP2ZGNRWvIWq1_ExnCxG-gBMBzeSRXTiIcBNmf3ylHD1UEKx7GLUr8KBhd_;li_sugr=364f0d68-561b-4eaa-aced-3b747e4dcc2d;li_theme=light;li_theme_set=app;liap=true;timezone=Asia/Bangkok;UserMatchHistory=AQKCJ6FDRptsEAAAAZjz31wgZIozzkggSreVA9WJqhglZzMxxVatQ0EYBrV8d3vfqZgjcAR-Hewr9M-aToggbHLXAl73HWCMeOgcHWbqdXq4ZW3EvL_dGnucgzhn7E9VTZ_XubyQQH7Er_d-qDHktn06ETx4gS1lG7px345YrOf0uPuAf27Po11gkgzFUbQHaCyDt38qgjId6OcrS3pdqJ7rBabPoz3Wvk_hSVY4kKH54bxfM58yi8AW3RvMBYcrFuOK9CGNXm5HM3qSizIAxrI1rHPEsQ0R7HmHGie7WfqnfZIB4DdlalAO-vhkIuFi7wmHfhoCrWikC20K8aVZkjz07heNR4d0dC-ljcwvJ-D89VzfKw'

url = "https://www.linkedin.com/in/luavietsg/"
slug = "luavietsg"
p = get_target_id(cookie, slug, url)
print(p)
