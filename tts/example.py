from gtts import gTTS
import os
import requests
from requests.structures import CaseInsensitiveDict
import json

url = "http://localhost:5005/webhooks/rest/webhook"
language = 'en'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = {
    "sender": "joao_test",
    "message": "/get_name{\"name\":\"test\"}"
}

resp = requests.post(url, headers=headers, json=data)
resp = str(resp.text).replace('[', '').replace(']', '')
pos = json.loads(resp)
mytext = pos['text']
print(mytext)


ttsobj = gTTS(text=mytext, lang=language, slow=False)
ttsobj.save("audio.mp3")
os.system("mpg321 audio.mp3")
