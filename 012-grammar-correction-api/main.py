# Using grammar api at: https://languagetool.org/http-api/#/default

import requests
import json

url = "https://api.languagetool.org/v2/check"
data = {
    "text": "Tis is a nixe day",
    "language":"auto"
}
response = requests.post(url, data=data)
# json.loads converts string into a dictionary
result = json.loads(response.text)
print(result)