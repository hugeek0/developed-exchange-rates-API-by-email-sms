BASE_PATH = "*****************************"
API_KEY = "******************************"
url = BASE_PATH + API_KEY

KAVENEGAR_API_KEY = "*********************"

rules = {
    "archive": True,
    "mail": {
        "enable" : True,
        "receiver_email": "*****************************",
        "sender_email": "****************************",
        "app_password": "******************",
        "preferred": ["CAD", "USD", "BTC", "IRR"]
    },

    "notification": {
        "enable": True,
        "receiver": "09*********",
        "preferred":{
            "CAD": {"min": "********", "max": "*******"},
            "IRR": {"min": "*****", "max": "********"}
        }

    }

}
