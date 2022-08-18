# 依存関係を定義
# 要: pip install requests
import requests

API_URL = "https://xxxxxxx/dev"

params = {
    'text': 'こんにちは'
}

response = requests.get(API_URL, params=params)

print(response.text)
