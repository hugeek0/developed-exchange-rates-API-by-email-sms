from config import url,rules
import requests
import json
from mail import send_smtp_email
from notification import send_sms
from datetime import datetime
from khayyam import JalaliDatetime


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(file_name, rates):
    with open(f"archive/{file_name}.json", "w") as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    subject = f"{timestamp} rates"
    if rules["mail"]["preferred"] is not None:
        tmp = dict()
        for exc in rules["mail"]["preferred"]:
            tmp[exc] = rates[exc]
        rates = tmp

    body = json.dumps(rates)

    send_smtp_email(subject, body)


def check_notification(rates):
    msg = ""
    preferred = rules["notification"]["preferred"]
    for exc in preferred.keys():
        if rates[exc] <= exc["min"]:
            msg += f"{exc} reached min: {rates[exc]}"
        if rates[exc] >= exc["max"]:
            msg += f"{exc} reached max: {rates[exc]}"

    return msg


def send_notification(msg):
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    msg += now
    send_sms(msg)


if __name__ == "__main__":
    res = get_rates()
    if rules["archive"]:
        archive(res["timestamp"],res["rates"])

    if rules["mail"]["enable"]:
        send_mail(res["timestamp"], res["rates"])

    if rules["notification"]["enable"]:
        notification_msg = check_notification(res["rates"])
        if notification_msg:
            send_notification(notification_msg)
