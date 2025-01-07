import json
import pandas as pd
from settings import config
from datetime import datetime
from urllib.parse import urlparse
from google.oauth2 import service_account
from app.persistence.db import get_bg_client


def etl_bigquery():
  # Extract
  df = pd.read_csv('posts.csv')
  with open("domain_data.json", "r", encoding="utf-8") as f:
    domains = json.load(f)
  
  # Transform
  df = df.rename(columns={'Title': 'title', 'URL': 'url'})
  df[["domain", "whois_status", "domain_created", "expiry_date"]] = (
    df.apply(process_domain, axis=1, args=(domains,), result_type='expand')
  )
  
  # Load
  credentials = service_account.Credentials.from_service_account_file(
    'bg-key.json'
  )
  df.to_gbq(
    f"{config.GCP_BQ_DATASET}.{config.GCP_BQ_TABLE}", 
    if_exists='replace', 
    credentials=credentials,
    project_id=config.GCP_PROJECT_ID
  )
  
  
def process_domain(row: pd.Series, domains: dict) -> pd.Series:
  """
  Process a single row of the dataframe, extracting the domain, its creation date, expiry date and a flag indicating if the whois status is valid.
  
  Parameters
  ----------
  row : pd.Series
    The row to process.
  domains : dict
    The JSON object containing the domain data.
  
  Returns
  -------
  pd.Series
    A pandas Series with the following columns:
      - whois_status: a boolean indicating if the whois status is valid.
      - domain_created: the creation date of the domain.
      - expiry_date: the expiry date of the domain.
  """
  expiry_date = None
  domain_created = None
  whois_status = False
  
  domain = urlparse(row.url).netloc
  
  if domain not in domains['data']:
    return pd.Series(
      [domain, whois_status, domain_created, expiry_date], 
      index=["domain", "whois_status", "domain_created", "expiry_date"]
    )
  
  for item in domains['data'][domain]:
    print(f"valid domain {domain}")
    if len(item) == 0:
      continue
    key, value = item.popitem()
    if value.find("Registry Expiry Date:") != -1:
      expiry_date = value.split(": ")[1].strip()
    if value.find("Created Date:") != -1 or value.find("Creation Date:") != -1:
      domain_created = value.split(": ")[1].strip()
      
  whois_status = expiry_date is not None or domain_created is not None
  return pd.Series(
    [domain, whois_status, domain_created, expiry_date], 
    index=["domain", "whois_status", "domain_created", "expiry_date"]
  )
  
  