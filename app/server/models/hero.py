from pydantic import BaseModel


class Attributes(BaseModel):
    agigain: float
    attackbackswing: float
    attackpoint: float
    attackrange: int
    attacktype: str
    baseagi: int
    basearmor: int
    baseattacktime: float
    basedmg: int
    baseint: int
    basemagicres: float
    basemovespeed: int
    basestr: int
    daysight: int
    intgain: float
    nightsight: int
    strgain: float
    turnrate: float

    class Config:
        schema_extra = {
            "example": {
                "basestr": 19,
                "baseagi": 11,
                "baseint": 22,
                "strgain": 2.1,
                "agigain": 1.2,
                "intgain": 3.3,
                "basedmg": 37,
                "basearmor": 2,
                "basemagicres": 0.25,
                "basemovespeed": 315,
                "attacktype": "Ranged",
                "attackrange": 380,
                "attackpoint": 0.35,
                "attackbackswing": 0.366,
                "baseattacktime": 1.7,
                "turnrate": 0.6,
                "daysight": 1800,
                "nightsight": 800
            }
        }


class Roles(BaseModel):
    carry: int
    complexity: int
    disabler: int
    durable: int
    escape: int
    initiator: int
    jungler: int
    nuker: int
    pusher: int
    support: int

    class Config:
        schema_extra = {
            "example": {
                "carry": 0,
                "nuker": 3,
                "initiator": 0,
                "disabler": 0,
                "durable": 0,
                "escape": 0,
                "support": 0,
                "pusher": 0,
                "jungler": 0,
                "complexity": 1
            }
        }


class Hero(BaseModel):
    _id: str
    attributes: Attributes
    roles: Roles

    class Config:
        schema_extra = {
            "example": {
                "heroname": "zeus",
                "attributes": {
                    "basestr": 19,
                    "baseagi": 11,
                    "baseint": 22,
                    "strgain": 2.1,
                    "agigain": 1.2,
                    "intgain": 3.3,
                    "basedmg": 37,
                    "basearmor": 2,
                    "basemagicres": 0.25,
                    "basemovespeed": 315,
                    "attacktype": "Ranged",
                    "attackrange": 380,
                    "attackpoint": 0.35,
                    "attackbackswing": 0.366,
                    "baseattacktime": 1.7,
                    "turnrate": 0.6,
                    "daysight": 1800,
                    "nightsight": 800
                },
                "roles": {
                    "carry": 0,
                    "nuker": 3,
                    "initiator": 0,
                    "disabler": 0,
                    "durable": 0,
                    "escape": 0,
                    "support": 0,
                    "pusher": 0,
                    "jungler": 0,
                    "complexity": 1
                }
            }
        }
