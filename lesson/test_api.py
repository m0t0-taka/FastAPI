import requests
import json


def main():
    url = 'http://127.0.0.1:8000/item/'
    body = {
        "name": "book",
        "description": "good",
        "price": 1200,
        "tax": 1.1
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()

# このファイルを実行
# →mainが叩かれる
# →指定したurlにrequestが送られる
# →main.pyに入りreturnされる
