import json
from typing import List
import requests
from urllib.parse import urlparse
from app.models.post import Post
from settings import config


def get_data_from_whois_api(posts: List[Post]):
  url = config.RAPIDAPI_URL
  headers = {
      "x-rapidapi-key": config.RAPIDAPI_KEY,
      "x-rapidapi-host": config.RAPIDAPI_HOST
  }
  results = {}

  # Split the posts into groups of 5 because the API has a limit of certain domains per request
  for i in range(0, len(posts), 5):
      group_posts = posts[i:i+5]
      domains = [urlparse(post.url).netloc for post in group_posts]
      querystring = {"domains": ",".join(domains), "format": "split"}

      response = requests.get(url, headers=headers, params=querystring)

      if response.status_code == 200:
          data = response.json()
          results.update(data)
      else:
          print(f"Error: {response.status_code}")
          
  # Write results to a JSON file
  with open("domain_data.json", "w") as f:
      json.dump({"data": results}, f, indent=2)
          