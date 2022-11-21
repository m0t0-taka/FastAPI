import requests
import json


def main():
    url = 'https://y7c0s3.deta.dev'
    data = {
        'x': 2,
        'y': 3
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == '__main__':
    main()
