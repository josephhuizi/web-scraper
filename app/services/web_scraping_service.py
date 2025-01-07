import requests 
from settings import config
from typing import List
from bs4 import BeautifulSoup
from app.models.post import Post

def get_data_from_website() -> List[Post]:
  url = config.WEBSITE_URL
  response = requests.get(url)

  if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')

      posts: List[Post] = []
      for post in soup.find_all('tr', class_='athing'):
          anchor = post.find('span', class_='titleline').find('a')
          title = anchor.text
          url = anchor['href']
          if title is not None and url is not None:
            posts.append(Post(title=title, url=url))
          
      return posts
  else:
      print("Failed to retrieve the webpage")