from pydantic import BaseModel


class UserBase(BaseModel):
    nom: str
    email: str
    type_utilisateur: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    actif: bool

    class Config:
        from_attributes = True