from pydantic import BaseModel, Field
from typing import Literal
from enum import Enum

class TailleEnum(str, Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class Order(BaseModel):
    article: str
    taille: TailleEnum
    couleur: str
    quantite: int = Field(default=1, ge=1)
