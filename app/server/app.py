from fastapi import FastAPI, HTTPException
from .routes.attributesRoute import attributes
from .routes.searchRoute import search
from .routes.heroesRoute import heroes
from .routes.compareRoute import compare
from .routes.rolesRoute import roles
from .models.hero import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Welcome"])
async def Welcome():
    return {"message": "Welcome to DotaDictionary! changes done"}

app.include_router(heroes)
app.include_router(roles)
app.include_router(attributes)
app.include_router(search)
app.include_router(compare)
