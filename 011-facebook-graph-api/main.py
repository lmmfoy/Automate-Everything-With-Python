import requests
import json

# Getting specific photo from facebook posts
url = "https://graph.facebook.com/v15.0/{image_id}?fields=link%2Cimages&access_token={access_token}"

response = requests.get(url)
data = response.text
data = json.loads(data)
img_url = data["images"][0]["source"]

img_bytes = requests.get(img_url).content

with open("image.jpg", "wb") as file: 
    file.write(img_bytes)