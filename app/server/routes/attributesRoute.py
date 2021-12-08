from ..database import get_client
from fastapi import APIRouter, HTTPException

attributes = APIRouter()


@attributes.get("/attributes", tags=["Attributes"])
async def get_allAttributes():
    allattributes = None
    try:
        collection = await get_client()["dotadictionary"]['heroes']
        allattributes = await collection.find_one({})
        allattributes = {'attributes': list(
            allattributes['attributes'].keys())}
    except Exception:
        raise HTTPException(
            status_code=408, detail="Connection to database failed... :-(")
    return allattributes


@attributes.get("/hero/attributes/{heroname}", tags=["Attributes"])
async def get_allHeroAttributes(heroname: str):
    herodetails = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find_one(
            {'_id': heroname.lower()}, {'_id': 0, 'roles': 0})
        herodetails['heroname'] = heroname
        herodetails['attributes'] = herodetails.pop('attributes')
    except Exception:
        raise HTTPException(
            status_code=404, detail="Hero not found. Please request with valid Hero name.")
    return herodetails


@attributes.get("/hero/attributes/{heroname}/{attribute}", tags=["Attributes"])
async def get_HeroAttribute(heroname: str, attribute: str):
    herodetails = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find_one(
            {'_id': heroname.lower()}, {'_id': 0, 'roles': 0})
        herodetails['heroname'] = heroname.lower()
        herodetails[attribute] = herodetails.pop('attributes')[attribute]
    except Exception:
        raise HTTPException(
            status_code=404, detail="Hero not found. Please request with valid Hero name.")
    return herodetails
