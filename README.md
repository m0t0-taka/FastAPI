### env

- Python 3.9.7

### Installation

`pip3 install fastapi`

##### サーバー

`pip3 install uvicorn`

### サーバー起動

例) main ファイルの app インスタンスを起動。--reload を付けることでホットリロード

`uvicorn main:app --reload`

Uvicorn running on http://127.0.0.1:8000

/docs とすることで自動生成ドキュメントを確認できる
