from ..database import get_client
from fastapi import APIRouter, HTTPException

roles = APIRouter()


@roles.get("/roles", tags=["Roles"])
async def get_allRoles():
    allroles = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        allroles = collection.find_one({})
        allroles = {'allroles': list(allroles['roles'].keys())}
    except Exception:
        raise HTTPException(
            status_code=408, detail="Connection to database failed... :-(")
    return allroles


@roles.get("/hero/roles/{heroname}", tags=["Roles"])
async def get_allHeroRoles(heroname: str):
    herodetails = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find_one(
            {'_id': heroname}, {'_id': 0, 'attributes': 0})
        herodetails['heroname'] = heroname.lower()
        herodetails['roles'] = herodetails.pop('roles')
    except Exception:
        raise HTTPException(
            status_code=404, detail="Hero not found. Please request with valid Hero name.")
    return herodetails


@roles.get("/hero/roles/{heroname}/{role}", tags=["Roles"])
async def get_HeroRole(heroname: str, role: str):
    herodetails = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find_one(
            {'_id': heroname.lower()}, {'_id': 0, 'attributes': 0})
        herodetails['heroname'] = heroname.lower()
        herodetails[role] = herodetails.pop('roles')[role]
    except Exception:
        raise HTTPException(
            status_code=404, detail="Hero not found. Please request with valid Hero name.")
    return herodetails
