
from ..database import get_client
from fastapi import APIRouter, HTTPException, Request, Query
from typing import Optional

search = APIRouter()


@search.get("/search/heroes/", tags=["Search"])
def get_SpecificHeroes(request: Request, carry: Optional[int] = Query(None, description='0 or 1 or 2 or 3'),
                       nuker: Optional[int] = Query(None, description='0 or 1 or 2 or 3'), initiator: Optional[int] = Query(None, description='0 or 1 or 2 or 3'),
                       disabler: Optional[int] = Query(None, description='0 or 1 or 2 or 3'), durable: Optional[int] = Query(None, description='0 or 1 or 2 or 3'),
                       escape: Optional[int] = Query(None, description='0 or 1 or 2 or 3'), support: Optional[int] = Query(None, description='0 or 1 or 2 or 3'),
                       pusher: Optional[int] = Query(None, description='0 or 1 or 2 or 3'), jungler: Optional[int] = Query(None, description='0 or 1 or 2 or 3'),
                       complexity: Optional[int] = Query(None, description='0 or 1 or 2 or 3'), attacktype: Optional[str] = Query('any', description='Melee or Ranged')):
    allsuchheroes = None
    try:
        # print(dict(request.query_params))
        collection = get_client()["dotadictionary"]['heroes']
        query_params = dict(request.query_params)
        search_dict = {}
        if attacktype.lower().strip() in ['ranged', 'melee']:
            search_dict['attributes.attacktype'] = attacktype[0].upper() + \
                attacktype[1:].lower()
        for key in query_params:
            if key != 'attacktype':
                search_dict['roles.'+key] = int(query_params[key])
        print(search_dict)
        allsuchheroes = collection.find(search_dict).distinct('_id')
        allsuchheroes = {'heroes': list(allsuchheroes)}
    except Exception:
        raise HTTPException(
            status_code=404, detail="No Heroes found with such options. Please try again with other options.")
    if len(allsuchheroes['heroes']) == 0:
        raise HTTPException(
            status_code=404, detail="No Heroes found with such options. Please try again with other options.")
    return allsuchheroes
