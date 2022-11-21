from typing import Optional  # option parameter
from fastapi import FastAPI
from pydantic import BaseModel, Field

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
# @app.get("/countries/{country_name}")
# async def country(country_name: str = "japan", city_name: str = "tokyo"):
#     return {
#         "country_name": country_name,
#         "city_name": city_name
#     }
# ↑このときのpath
# http://127.0.0.1:8000/countries/america?city_name=new_york


# option parameter（必須でないparameter）
# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }


# BaseModelを継承したItem classを作成
# postは以下のようなrequest bodyを作成する必要がある
class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


# インスタンス化
app = FastAPI()


@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込み価格{int(item.price*item.tax)}円"}
