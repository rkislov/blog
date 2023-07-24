from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog


router = APIRouter()


@router.post("/blog", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async  def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog,db=db,author_id="81a7052e-ad20-42f9-be52-6067be9e5cd2")
    return blog