from ..database import get_client
from fastapi import APIRouter, HTTPException
from typing import Optional

compare = APIRouter()


@compare.get("/hero/compareRole/{hero1}/{hero2}/{role}", tags=["Compare"])
async def get_WinnerHeroRole(hero1: str, hero2: str, role: str):
    winner = None
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find(
            {'_id': {'$in': [hero1, hero2]}}, {'roles.'+role: 1})

        if herodetails[0]['_id'] == hero1:
            if(herodetails[0]['roles'][role] > herodetails[1]['roles'][role]):
                winner = hero1
            else:
                winner = hero2
        else:
            if(herodetails[0]['roles'][role] > herodetails[1]['roles'][role]):
                winner = hero2
            else:
                winner = hero1
    except Exception:
        raise HTTPException(
            status_code=404, detail="Role not found. Please request with valid Role.")
    return {"winner": winner}


@compare.get("/hero/compareAttribute/{hero1}/{hero2}/{attribute}", tags=["Compare"])
def get_WinnerHeroAttribute(hero1: str, hero2: str, attribute: str):
    winner = None
    if attribute == 'attacktype':
        raise HTTPException(
            status_code=404, detail="Attack type cannot be compared")
    try:
        collection = get_client()["dotadictionary"]['heroes']
        herodetails = collection.find(
            {'_id': {'$in': [hero1, hero2]}}, {'attributes.'+attribute: 1})

        if herodetails[0]['_id'] == hero1:
            if(herodetails[0]['attributes'][attribute] > herodetails[1]['attributes'][attribute]):
                winner = hero1
            else:
                winner = hero2
        else:
            if(herodetails[0]['attributes'][attribute] > herodetails[1]['attributes'][attribute]):
                winner = hero2
            else:
                winner = hero1
    except Exception:
        raise HTTPException(
            status_code=404, detail="Attribute not found. Please request with valid Attribute.")
    return {"winner": winner}
