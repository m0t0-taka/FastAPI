from fastapi import FastAPI

# インスタンス化
app = FastAPI()


@app.get("/")  # デコレータ /にgetでアクセスがあったら以下を実行
async def index():
    return {"message": "Hello World"}
