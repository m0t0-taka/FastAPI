from fastapi import FastAPI

# インスタンス化
app = FastAPI()

# path parameter
# @app.get("/countries/{country_name}")  # デコレータ ()内のpathにgetでアクセスがあったら以下を実行
# async def country(country_name: str):
#     return {"country_name": country_name}

# query parameter
# path parameterに無い引数を与えるとquery parameterになる
# @app.get("/countries/")
# async def country(country_name: str = "japan", country_no: int = 1):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }
# ↑このときのpath
# http://127.0.0.1:8000/countries/?country_name=america&counry_no=3


# path parameter & query parameter
@app.get("/countries/{country_name}")
async def country(country_name: str = "japan", city_name: str = "tokyo"):
    return {
        "country_name": country_name,
        "city_name": city_name
    }
# ↑このときのpath
# http://127.0.0.1:8000/countries/america?city_name=new_york
