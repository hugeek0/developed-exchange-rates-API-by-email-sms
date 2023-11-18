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
            "CAD": {"min": "1.480000", "max": "1.500000"},
            "IRR": {"min": "46000", "max": "46500"}
        }

    }

}