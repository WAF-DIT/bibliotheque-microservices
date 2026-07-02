from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    available: bool

    class Config:
        from_attributes = True