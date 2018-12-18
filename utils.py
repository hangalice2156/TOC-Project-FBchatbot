import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAbkMw3Nx4YBAORAcz51WSV9ldgDJWmGKZApPREbd0oZAEYoEHiRCBh0jM96Bo8OY4KZAVZAWuB0XyDreDq6OZBAqZB84TnTnOGEVth5jYE8AVEwZB5jAW8mURuR4Ye0CC8TcOtR8Wuj313Cj9rnPKnmyFBDWyW51eIoOOSshDVrNwcgCBlnXMh"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_img_message(id,text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"attachment": {"type": "image", "payload": {"url": text}}}
    }
    response = requests.post(url, json=payload)
    
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
