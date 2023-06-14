import asyncio

import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from db.db import engine
from models.person_model import Base
from schemas.mutation import Mutation
from schemas.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    print("Populating database...")
    asyncio.run(create_tables(engine))
    print("Database populated.")

    print("Starting server...")
    uvicorn.run("main:application", host='0.0.0.0', port=8000, reload=True)
