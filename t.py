import re
import requests
from headers import get_header


def check_type(url):
    if "linkedin.com/company/" in url:
        return "COMPANY"
    elif "linkedin.com/in/" in url:
        return "PROFILE"
    return None


def get_query_id(cookie: str, url):
    headers = get_header(cookie, url)
    html = requests.get(url, headers=headers).text
    with open("output.txt", "w", encoding="utf-8") as f:
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


cookie = 'lms_ads=AQHf4fJNYdGBmwAAAZjpVGU4XdUgUu8sOg9Lw1v-ejf8e-wNnJwp9sHEdQZuaXxzawVZuf9qA71H9u3EZKM3dxzl87XojbZ7;_guid=3a1c3758-9502-44e6-90ad-872df1bfb750;li_theme_set=app;bcookie="v=2&1f486571-bb5c-4853-8dee-ae2236f31af0";__cf_bm=0M_IZK1LFdvMIVCqy1ucYmIUtoJRa6xijZiSdrGNvE4-1756358680-1.0.1.1-Yx5dUAU6tqorJJC9LKRrF7wQIBg01rB6QqNXTE73OgMY2opgOkOe8YX8X1OHzt9Uxisy0lsluO4ZjkmjzCcwczvAZpWj.nD78J_Q6jRAiRE;_gcl_au=1.1.1039331792.1756000425.9343464.1756286035.1756286034;bitmovin_analytics_uuid=70e17664-3618-4bb8-aaf8-2c593168684b;lms_analytics=AQHf4fJNYdGBmwAAAZjpVGU4XdUgUu8sOg9Lw1v-ejf8e-wNnJwp9sHEdQZuaXxzawVZuf9qA71H9u3EZKM3dxzl87XojbZ7;AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1;fptctx2=taBcrIH61PuCVH7eNCyH0I1otfYAPn9VOPY9aMX8tO1bhLtw1gQK9xHJJhl%252bqMZ%252bcSypoBH9jiFLRHSLApZiIl3k6iThlZdQ5GXm7ZDrO8he%252fx7m36rHdnoNBiYChmdlR7RJP8SQ2DE0IpSmhgqsdBo0jm5Al1oZsRV47tP31CVZjRBvHpUg3Ko%252fnBRE4IJTPpObFakoIjwcFDa9c3PcAzRiJTrpvs5f%252bQicKQd50Hsr6f%252fM8IZIH0iOt2TcUNPCEwy8zKBK6XGhArozx0Im8yjp0aT2uEiN0QXqS7OzgCKVgZz1GWdP7QOAx4zuCnNpHgt2y771qQGhkDS1BoV%252brMys7%252f%252fFFh9bP80s2yLguZLKNLy10mPTftPfAvqXYy5P2vxIbq%252fIqvrH2EHCcovGyg%253d%253d;li_at=AQEDAUf9ZWACn3s8AAABlP-uFD0AAAGZCAw4iE4AP-PJ43Xn9PW8lJL2E8cJI_EFtAUPRoLuG9mIT6SJCxp5zo1uR07dIIl95Y3z6vL8wYjZYsclf7GK2j-NfSefN6cIivpclrqM4zhBW0ICoe-I_LWq;lang=v=2&lang=en-us;lidc="b=OB96:s=O:r=O:a=O:p=O:g=3816:u=55:x=1:i=1756358948:t=1756437702:v=2:sig=AQHqJCsnF_kwlxlUbY7rtDa02coWXoRy";aam_uuid=06176110973161480230860678494130966861;AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20328%7CMCMID%7C06026700597502077400810245217340646022%7CMCAAMLH-1756962667%7C3%7CMCAAMB-1756962667%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756365067s%7CNONE%7CMCCIDH%7C-1845589424%7CvVersion%7C5.1.1;AnalyticsSyncHistory=AQI4-l8Rx8DbLQAAAZjpVGRIAcrEIYqSlyJaxJd-hsakUpWv03WWzUoZiCbgzMaqiO7bn2JPx8-TwFvPc2U90w;bscookie="v=1&20250209062556bcb96a5f-b68a-4988-8c48-7c7de9c5abd0AQHj3_28HKyPApTj89XIlYER2ktllwTw";dfpfpt=9f2313db6b3543f8922b7b4bb9173160;JSESSIONID="ajax:4248487920917906119";li_rm=AQFB-AqJ3YVdLwAAAZT_rfGH7a-XPJuy4pibkcbxXwPog2dnsK0p0Qpuwt5nXizJGP3CxGthfXTskHeIhsVgOTIql_p-7JNxDoI6b9sc1iLBeO4ICxilZGIt;li_sugr=ccd9e700-016a-45eb-ab27-761e0c215d4a;li_theme=light;li_theme_set=app;liap=true;timezone=Asia/Bangkok;UserMatchHistory=AQKXjpgZDjMOGQAAAZjvJrQDDfhBuBBi8sRhdc20UqByi6M0Mq-0DB-XQDRu2tULx6bfPaSDElRXyK_RV8Q859iaNtUFCx7skZ0nKfg0pcOFR3-s3qCzwQ175xFjqaUVb_7mZWINUWfYi3xmJXb847XmaIpBV2TicUP-xLp2OvckqPz3ruGhGy3i2Xlfrm5x90xQliSgIAvroYsW438vEbpn-0qSEHFKlZgHhWDnypHj3LgOLsBKIPq7eyEnq5OTwhrAOA0f7ZAjRFQGGDJSevyZUdgnv3UakvOq4GSY6u08SiEytuFGqKP3emHQ3iVq_0OfQs9oUhUhS4h40WBH99ePZF-i75VSKTBJXC2S8rKWnwGnzQ'
url = "https://www.linkedin.com/company/fivi-agency/"


qi = get_query_id(cookie, url)
print(qi)
