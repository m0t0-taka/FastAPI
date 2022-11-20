from fastapi import FastAPI

# インスタンス化
app = FastAPI()


@app.get("/countries/{country_name}")  # デコレータ ()内のpathにgetでアクセスがあったら以下を実行
async def country(country_name: str):
    return {"country_name": country_name}
