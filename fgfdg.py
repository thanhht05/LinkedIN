# import requests

# cookies = {
#     "LOGIN_INFO": "AFmmF2swRAIgGy0gUvrUcf-djh0dgY7YCGDRd6dG7QM-ePiGbr8q5w4CIGWynqVmkVNf0vObcjR0aWzmP3Iywosfq7PqhkEaGOXr:QUQ3MjNmeE9RWVh6bF9naGR6bk9NU2tzUGlEMzhlVUotUVlsRFJISTdfRG5JNmI0S2tBX3BYVm9nbVA2czFxUzdTVU9FeUJVcWZ5WkkyYUNpXzRQODBKYWx5WnhrOUthT2NQSDc4MkR4NHZHemJOaHpJeGtIeW8tSlJ4dGc4OTNPdHh2NFZ2MktRY3FyUDlKTVhGdWVfdmFsUGhYVmtNUTFB",
#     "VISITOR_INFO1_LIVE": "nkk5cxyHWLE",
#     "VISITOR_PRIVACY_METADATA": "CgJWThIEGgAgRw%3D%3D",
#     "PREF": "tz=Asia.Bangkok&f4=4000000&f6=40000000&f7=100",
#     "HSID": "ARjkEIDjDwgldeAsz",
#     "SSID": "Ae0ID1fXryMt-HdMy",
#     "APISID": "PWzvOAYyh6UcwWEm/ABbUhDurnfqj6-O3D",
#     "SAPISID": "F0JyCqEcZDquxfGF/AXWQJkKyHyYMzZmVJ",
#     "__Secure-1PAPISID": "F0JyCqEcZDquxfGF/AXWQJkKyHyYMzZmVJ",
#     "__Secure-3PAPISID": "F0JyCqEcZDquxfGF/AXWQJkKyHyYMzZmVJ",
#     "SID": "g.a0000wjL_BT8uxKq3x_B8LaL9PCWpsucEKCVoWF_n-S8X2YoGy7F4dAfFsSbJUBlzsiBpbbUmAACgYKAagSARUSFQHGX2MivFp1td2gdKquCyHohigdsRoVAUF8yKoycustq_N7bkidw7Ba2Evj0076",
#     "__Secure-1PSID": "g.a0000wjL_BT8uxKq3x_B8LaL9PCWpsucEKCVoWF_n-S8X2YoGy7FoKt4_QTIbZC9XPpy6veH8AACgYKAY0SARUSFQHGX2MisHZWPa04Kzqz3y7F2peolBoVAUF8yKooXZ3XTaCBn-BhBrh1sRvl0076",
#     "__Secure-3PSID": "g.a0000wjL_BT8uxKq3x_B8LaL9PCWpsucEKCVoWF_n-S8X2YoGy7FpkArlEek8U0xL9EZ5bf9JQACgYKAdUSARUSFQHGX2Mi2S3vuuKG5zbk9GVH48oqeBoVAUF8yKq3WVgoTrlazXPg9w2oMIcC0076",
#     "YSC": "sZqUVeK_LsY",
#     "__Secure-ROLLOUT_TOKEN": "CPTx7fKmlLTwqAEQ-q_ugJ3AjgMYndm3weatjwM%3D",
#     "__Secure-1PSIDTS": "sidts-CjIB5H03P5s6wJCBkIGvW6CWYjcFAjgVZsQM5hC_fe-epNYi28G_cimh-Z811m1L20L-QxAA",
#     "__Secure-3PSIDTS": "sidts-CjIB5H03P5s6wJCBkIGvW6CWYjcFAjgVZsQM5hC_fe-epNYi28G_cimh-Z811m1L20L-QxAA",
#     "SIDCC": "AKEyXzU3P3ZY43qypmBV1lxEHDytQ-rh-k7bN8LGWsPYjFMdzFGGCOh9J91Of2X9zYIWeyyZVw",
#     "__Secure-1PSIDCC": "AKEyXzW4rtldNLoee9hFdpYKMxXgP-ZPT3zgpdQ9BgQptFcUjXobY6p7oYTveSWW68ONXU1p7A",
#     "__Secure-3PSIDCC": "AKEyXzWkD0J0XPtQWODNUNQWCbtjuNqPjW4yZsv0gIZ147sAGeNdop3PMuTDYxJdfimF7xYVIQ",
#     "ST-163o2bb": "session_logininfo=AFmmF2swRAIgGy0gUvrUcf-djh0dgY7YCGDRd6dG7QM-ePiGbr8q5w4CIGWynqVmkVNf0vObcjR0aWzmP3Iywosfq7PqhkEaGOXr%3AQUQ3MjNmeE9RWVh6bF9naGR6bk9NU2tzUGlEMzhlVUotUVlsRFJISTdfRG5JNmI0S2tBX3BYVm9nbVA2czFxUzdTVU9FeUJVcWZ5WkkyYUNpXzRQODBKYWx5WnhrOUthT2NQSDc4MkR4NHZHemJOaHpJeGtIeW8tSlJ4dGc4OTNPdHh2NFZ2MktRY3FyUDlKTVhGdWVfdmFsUGhYVmtNUTFB",
#     "CONSISTENCY": "AKreu9uPl1qj7DIVGECQqsvNvoKUA80S9L95Gs_xa7EfrQavhQRvLxOeC5hrkORAGp9cLzFFRZ0oIUfmaqgjq8imULA_tjlLBUgWciJ0_35to6-Cf7OBLnsUNiM",
#     "ST-4n4ru8": "session_logininfo=AFmmF2swRAIgGy0gUvrUcf-djh0dgY7YCGDRd6dG7QM-ePiGbr8q5w4CIGWynqVmkVNf0vObcjR0aWzmP3Iywosfq7PqhkEaGOXr%3AQUQ3MjNmeE9RWVh6bF9naGR6bk9NU2tzUGlEMzhlVUotUVlsRFJISTdfRG5JNmI0S2tBX3BYVm9nbVA2czFxUzdTVU9FeUJVcWZ5WkkyYUNpXzRQODBKYWx5WnhrOUthT2NQSDc4MkR4NHZHemJOaHpJeGtIeW8tSlJ4dGc4OTNPdHh2NFZ2MktRY3FyUDlKTVhGdWVfdmFsUGhYVmtNUTFB",
# }

# headers = {
#     "accept": "*/*",
#     "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
#     "authorization": "SAPISIDHASH 1756394367_0bf9a678f796a89cbf68419c84a35ae4ce27a690_u SAPISID1PHASH 1756394367_0bf9a678f796a89cbf68419c84a35ae4ce27a690_u SAPISID3PHASH 1756394367_0bf9a678f796a89cbf68419c84a35ae4ce27a690_u",
#     "content-type": "application/json",
#     "origin": "https://www.youtube.com",
#     "priority": "u=1, i",
#     "referer": "https://www.youtube.com/@holmes694",
#     "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
#     "sec-ch-ua-arch": '"x86"',
#     "sec-ch-ua-bitness": '"64"',
#     "sec-ch-ua-form-factors": '"Desktop"',
#     "sec-ch-ua-full-version": '"139.0.7258.139"',
#     "sec-ch-ua-full-version-list": '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.139", "Chromium";v="139.0.7258.139"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-model": '""',
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-ch-ua-platform-version": '"19.0.0"',
#     "sec-ch-ua-wow64": "?0",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "same-origin",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
#     "x-browser-channel": "stable",
#     "x-browser-copyright": "Copyright 2025 Google LLC. All rights reserved.",
#     "x-browser-validation": "XPdmRdCCj2OkELQ2uovjJFk6aKA=",
#     "x-browser-year": "2025",
#     "x-client-data": "CJa2yQEIorbJAQipncoBCIXiygEIlaHLAQiFoM0BCP2lzgEIlITPAQjehM8BCPaFzwEIj4fPARjh4s4BGM6CzwEY2IbPAQ==",
#     "x-goog-authuser": "0",
#     "x-goog-visitor-id": "Cgtua2s1Y3h5SFdMRSiX5sHFBjIKCgJWThIEGgAgRw%3D%3D",
#     "x-origin": "https://www.youtube.com",
#     "x-youtube-bootstrap-logged-in": "true",
#     "x-youtube-client-name": "1",
#     "x-youtube-client-version": "2.20250821.07.00",
# }

# params = {
#     "prettyPrint": "false",
# }

# json_data = {
#     "context": {
#         "client": {
#             "hl": "vi",
#             "gl": "VN",
#             "remoteHost": "2402:800:6210:7a58:99b2:852:635e:b317",
#             "deviceMake": "",
#             "deviceModel": "",
#             "visitorData": "Cgtua2s1Y3h5SFdMRSiX5sHFBjIKCgJWThIEGgAgRw%3D%3D",
#             "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36,gzip(gfe)",
#             "clientName": "WEB",
#             "clientVersion": "2.20250821.07.00",
#             "osName": "Windows",
#             "osVersion": "10.0",
#             "originalUrl": "https://www.youtube.com/@holmes694?si=P3ziUdraDQ9qSepj",
#             "screenPixelDensity": 1,
#             "platform": "DESKTOP",
#             "clientFormFactor": "UNKNOWN_FORM_FACTOR",
#             "configInfo": {
#                 "appInstallData": "CJfmwcUGELnZzhwQ9quwBRCr-M4cEIHNzhwQtejPHBCRjP8SEPLfzxwQ_LLOHBDevM4cEPu0zxwQ4ujPHBDJ6M8cEO7czxwQh6zOHBCIh7AFEMXDzxwQ6OTPHBC9tq4FEOLUrgUQy9GxBRC45M4cEL2ZsAUQndfPHBDnr88cEMzfrgUQibDOHBDN0bEFEITnzxwQmZixBRCZjbEFEIqCgBMQu9nOHBCCj88cEJPdzxwQlP6wBRC24K4FEInrzxwQ2vfOHBCNzLAFEPDUzxwQmLnPHBCe0LAFELbpzxwQ4M2xBRCmmrAFEP7AzxwQ6YjPHBCNuM8cEInorgUQ18GxBRCu1s8cELfq_hIQndDPHBDE1s8cEPDjzxwQs5DPHBCir88cEJHdzxwQyfevBRC_288cENPhrwUQ4srPHBDbr68FEMeOzxwQvYqwBRCOtM8cKkhDQU1TTUJVcm9MMndETkhrQnJpVUVyUFE1Z3VQOUE3di13YlZfQUMxekFhSFRETEFnd1RZSVFQTGpBV3hTYkVUaVEwZEJ3PT0wAA%3D%3D",
#                 "coldConfigData": "CJfmwcUGEOy6rQUQxIWuBRC9tq4FEOLUrgUQgemuBRC9irAFEJ7QsAUQz9KwBRDj-LAFEKS-sQUQ18GxBRCvp84cEPyyzhwQzeLOHBDHjs8cEKKvzxwQxrHPHBCNuM8cEKnCzxwQ-cbPHBCd0M8cEPbRzxwQ2tPPHBDE1s8cEJ3XzxwQntfPHBCD2c8cEOLZzxwQ_dnPHBCD2s8cEPvazxwQv9vPHBDP4M8cEPDjzxwQ6OTPHBCz5s8cEMznzxwQyejPHBDi6M8cELbpzxwQievPHBoyQU9qRm94M0RMVTRIVVM4TndyNkx3M1liMjlPTW5mMGF3UFExTl9lbHY5MVBTbTFfMFEiMkFPakZveDJMY1JvZUFobkMzZk41S0hadnRObE5ka2lUdkZleVdLV1pORlljbVZvWnZRKpABQ0FNU1pnMHZ1TjIzQXFRWmx4LW9LclVFc2hDRGhab1F2UURaRFBrTzdnQVVxeDNhRWY0anlRUjYxQUxrQWhVOW1iRzNINFdrQlpHY0JiaUFBZ1NsMGdhaHFBU1RqUVdmZV9TSUJzaGF2MFc0QzczQUJqSzNLSkRmQnRta0JnUGMxQWFZRFpBZmxqaTdQQT09",
#                 "coldHashData": "CJfmwcUGEhQxMzMwNTU3Njc1MDE5MTAyODkwMxiX5sHFBjIyQU9qRm94M0RMVTRIVVM4TndyNkx3M1liMjlPTW5mMGF3UFExTl9lbHY5MVBTbTFfMFE6MkFPakZveDJMY1JvZUFobkMzZk41S0hadnRObE5ka2lUdkZleVdLV1pORlljbVZvWnZRQpABQ0FNU1pnMHZ1TjIzQXFRWmx4LW9LclVFc2hDRGhab1F2UURaRFBrTzdnQVVxeDNhRWY0anlRUjYxQUxrQWhVOW1iRzNINFdrQlpHY0JiaUFBZ1NsMGdhaHFBU1RqUVdmZV9TSUJzaGF2MFc0QzczQUJqSzNLSkRmQnRta0JnUGMxQWFZRFpBZmxqaTdQQT09",
#                 "hotHashData": "CJfmwcUGEhQxNzg3ODE2ODIzOTgzMTkyMDA2MxiX5sHFBiiU5PwSKKXQ_RIonpH-EijIyv4SKLfq_hIowYP_EiiRjP8SKMeAgBMoioKAEyipjIATKPeQgBMotZuAEyiFnoATKNKggBMouqKAEyi4pIATKM6kgBMo6KWAEyj0poATKO6ngBMyMkFPakZveDNETFU0SFVTOE53cjZMdzNZYjI5T01uZjBhd1BRMU5fZWx2OTFQU20xXzBROjJBT2pGb3gyTGNSb2VBaG5DM2ZONUtIWnZ0TmxOZGtpVHZGZXlXS1daTkZZY21Wb1p2UUI8Q0FNU0tBMElvdGY2RmE3QkJwTk44Z3E1Qk1rMEZSTGR6OElNeHFmdEM5ak5DYVhBQmRaWHVyQU4wVWc9",
#             },
#             "screenDensityFloat": 1.25,
#             "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
#             "timeZone": "Asia/Bangkok",
#             "browserName": "Chrome",
#             "browserVersion": "139.0.0.0",
#             "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#             "deviceExperimentId": "ChxOelUwTXpZMU5Ua3hPRFl3TXpjeE5qRTJPUT09EJfmwcUGGJfmwcUG",
#             "rolloutToken": "CPTx7fKmlLTwqAEQ-q_ugJ3AjgMYndm3weatjwM%3D",
#             "screenWidthPoints": 702,
#             "screenHeightPoints": 730,
#             "utcOffsetMinutes": 420,
#             "connectionType": "CONN_CELLULAR_4G",
#             "memoryTotalKbytes": "8000000",
#             "mainAppWebInfo": {
#                 "graftUrl": "https://www.youtube.com/@present2567",
#                 "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
#                 "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
#                 "isWebNativeShareAvailable": True,
#             },
#         },
#         "user": {
#             "lockedSafetyMode": False,
#         },
#         "request": {
#             "useSsl": True,
#             "internalExperimentFlags": [],
#             "consistencyTokenJars": [
#                 {
#                     "encryptedTokenJarContents": "AKreu9uPl1qj7DIVGECQqsvNvoKUA80S9L95Gs_xa7EfrQavhQRvLxOeC5hrkORAGp9cLzFFRZ0oIUfmaqgjq8imULA_tjlLBUgWciJ0_35to6-Cf7OBLnsUNiM",
#                     "expirationSeconds": "600",
#                 },
#             ],
#         },
#         "clientScreenNonce": "fFuRDbPzHTD0RFEc",
#         "clickTracking": {
#             "clickTrackingParams": "CB4QmysYASITCO-IvMHmrY8DFeFz9QUdR5oYxDIJY2hhbm5lbHM0",
#         },
#         "adSignalsInfo": {
#             "params": [
#                 {
#                     "key": "dt",
#                     "value": "1756394265069",
#                 },
#                 {
#                     "key": "flash",
#                     "value": "0",
#                 },
#                 {
#                     "key": "frm",
#                     "value": "0",
#                 },
#                 {
#                     "key": "u_tz",
#                     "value": "420",
#                 },
#                 {
#                     "key": "u_his",
#                     "value": "3",
#                 },
#                 {
#                     "key": "u_h",
#                     "value": "864",
#                 },
#                 {
#                     "key": "u_w",
#                     "value": "1536",
#                 },
#                 {
#                     "key": "u_ah",
#                     "value": "816",
#                 },
#                 {
#                     "key": "u_aw",
#                     "value": "1536",
#                 },
#                 {
#                     "key": "u_cd",
#                     "value": "24",
#                 },
#                 {
#                     "key": "bc",
#                     "value": "31",
#                 },
#                 {
#                     "key": "bih",
#                     "value": "730",
#                 },
#                 {
#                     "key": "biw",
#                     "value": "687",
#                 },
#                 {
#                     "key": "brdim",
#                     "value": "0,0,0,0,1536,0,1536,816,702,730",
#                 },
#                 {
#                     "key": "vis",
#                     "value": "1",
#                 },
#                 {
#                     "key": "wgl",
#                     "value": "true",
#                 },
#                 {
#                     "key": "ca_type",
#                     "value": "image",
#                 },
#             ],
#             "bid": "ANyPxKrcDwo6dCu3IQFL-C6kp7a6hPcUhAmr7geXOLrStfKZf28wi_Sl3iM2CBEa1mK0PZzCf28ldiiH7sGMQ909BB9sUcUyhA",
#         },
#     },
#     "channelIds": [
#         "UCxM5Kfydlazj9gg8CgfEmrA", ***
#     ],
#     "params": "EgIIAhgA",
# }

# response = requests.post(
#     "https://www.youtube.com/youtubei/v1/subscription/subscribe",
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )

# print(response.status_code)
# print(response.text)


# # channelIds => job_data["object_id"]


# # get job yt
# # import requests

# # headers = {
# #     'accept': 'application/json, text/plain, */*',
# #     'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
# #     'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NTYzOTQyMzUsImV4cCI6MTc4NzkzMDIzNSwibmJmIjoxNzU2Mzk0MjM1LCJqdGkiOiJDUGxrQVl3Vkkxc3dTOVhwIiwic3ViIjozMDYyNjg3LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.u1PxxZ7HJ3uDTEqRThGEFgEsu3Hf88Ta3U_kdgJ5ynU',
# #     'content-type': 'application/json;charset=utf-8',
# #     'origin': 'https://app.golike.net',
# #     'priority': 'u=1, i',
# #     'sec-fetch-dest': 'empty',
# #     'sec-fetch-mode': 'cors',
# #     'sec-fetch-site': 'same-site',
# #     't': 'VFZSak1VNXFUVFZPUkZreVRVRTlQUT09',
# #     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
# # }

# # params = {
# #     'account_id': '81494',
# # }

# # response = requests.get('https://gateway.golike.net/api/advertising/publishers/youtube/jobs', params=params, headers=headers)
