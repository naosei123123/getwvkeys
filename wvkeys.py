import requests
import env
import headers

def getKeys(license_url, pssh):
    api_url = env.getenv("api_url")

    headers.headers["X-API-Key"] = env.getenv("X-API-Key")

    payload = {
        "license_url": license_url,
        "pssh": pssh,
    }

    r = requests.post(api_url, headers=headers.headers, json=payload).text

    return r