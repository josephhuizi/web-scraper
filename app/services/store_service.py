import csv
import json
import os
from typing import List

from app.models.post import Post

def store_posts_csv(posts: List[Post]):
  try:
    with open('posts.csv', 'w', newline='', encoding="utf-8") as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(["Title", "URL"])
      writer.writerows([[post.title, post.url] for post in posts])
  except:
    pass

  