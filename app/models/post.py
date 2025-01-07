from pydantic import BaseModel


class Post(BaseModel):
  title: str
  url: str