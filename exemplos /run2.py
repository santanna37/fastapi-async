from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import uvicorn 
import asyncio
import databases 
from sqlalchemy import MetaData, Table, Column, Integer, String


#criar a conexão 
DATABASE_URL = "sqlite:///./schema.db"
database = databases.Database(DATABASE_URL)




# Fazer query
async def get_all_pessoas():
    query = PESSOA.select()
    result = await database.fetch_all(query) 
    return result


# APP e Rotas 
app = FastAPI()


@app.get("/")
async def read_root():
    await asyncio.sleep(20)
    return 

@app.get("/get")
async def read_data():
    await database.connect()
    people = await get_all_pessoas()
    print(people)

    formatted_pessoas = []
    for pessoa in people:
        formatted_pessoas.append(pessoa.name)

    await database.disconnect()
    return JSONResponse(
        content = {"pessoas": formatted_pessoas},
        status_code = 200
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)