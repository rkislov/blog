from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog
from uuid import UUID


def create_new_blog(blog: CreateBlog, db: Session, author_id:UUID = "81a7052e-ad20-42f9-be52-6067be9e5cd2"):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog