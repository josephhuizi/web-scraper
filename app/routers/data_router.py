from fastapi import APIRouter, Depends
from requests import request

from app.repositories import get_posts_repository
from app.repositories.posts_repository import PostRepository


router = APIRouter()

@router.get("/data")
async def root(
    limit: int = 10,
    offset: int = 0,
    post_repository: PostRepository = Depends(get_posts_repository)
):
    posts = post_repository.get_posts(limit, offset) 
    
    return posts