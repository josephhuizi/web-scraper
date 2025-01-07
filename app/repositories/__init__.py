from .posts_repository import PostRepository
from app.persistence.db import get_bg_client

def get_posts_repository() -> PostRepository:
  return PostRepository(client=get_bg_client())