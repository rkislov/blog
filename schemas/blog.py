from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date
from slugify import slugify
from uuid import UUID


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    photo: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = slugify(values.get("title"),allow_unicode=True)
        return values
    

class ShowBlog(BaseModel):
    id: UUID
    title: str
    slug: str
    content: Optional[str]
    photo: Optional[str] = None
    created_at: date

    class Config():
        orm_mode = True