# from ..database import hero_collection
from fastapi import APIRouter, HTTPException
from ..database import get_client


heroes = APIRouter()


@heroes.get("/heroes", tags=["Heroes"])
async def get_allHeroes():
    allheroes = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        allheroes = {'allheroes': collection.find().distinct('_id')}
    except Exception:
        raise HTTPException(
            status_code=408, detail="Connection to database failed... :-(")
    return allheroes


@heroes.get("/hero/alldetails/{heroname}", tags=["Heroes"])
async def get_allHeroDetails(heroname: str):
    herodetails = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find_one(
            {'_id': heroname.lower()}, {'_id': 0})
        herodetails['heroname'] = heroname
        herodetails['attributes'] = herodetails.pop('attributes')
        herodetails['roles'] = herodetails.pop('roles')
    except Exception:
        raise HTTPException(
            status_code=404, detail="Hero not found. Please request with valid Hero name.")
    return herodetails
