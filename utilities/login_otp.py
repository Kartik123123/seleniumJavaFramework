import requests

def get_otp(email):
    url = "https://retail-dev.vinecrms.com/api/api/"
    payload = {
        "type": "generate_otp_to_signin",
        "domain": "user",
        "email": email
    }
    response = requests.post(url, json=payload)

    response_json = response.json()

    otp = response_json["data"]["otp"]

    return otp
