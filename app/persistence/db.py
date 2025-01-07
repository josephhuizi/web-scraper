import pandas as pd
from settings import config
from google.oauth2 import service_account
from google.cloud import bigquery

def get_bg_client():
  try:
    credentials = service_account.Credentials.from_service_account_file(
        'bg-key.json'
    )
    return bigquery.Client(credentials= credentials,project=config.GCP_PROJECT_ID)
  except:
    print("Error loading credentials")
  