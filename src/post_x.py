import os
import requests
from requests_oauthlib import OAuth1

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

url = "https://api.twitter.com/2/tweets"
d978be3 (Add X auto post script and workflow)
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

tweet_text = "自動投稿テスト成功 🚀"

d978be3 (Add X auto post script and workflow)

response = requests.post(url, auth=auth, json=payload)

print(response.status_code)
print(response.text)
