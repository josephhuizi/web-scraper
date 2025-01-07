import pandas as pd
from google.cloud import bigquery
from settings import config

class PostRepository:
    def __init__(self, client):
        self.client = client

    def get_posts(self, limit=None, offset=None):
        query = f"""
            SELECT domain, whois_status, title, url, expiry_date, domain_created
            FROM `{config.GCP_PROJECT_ID}.{config.GCP_BQ_DATASET}.{config.GCP_BQ_TABLE}`
        """

        if limit is not None:
            query += f" LIMIT {limit}"

        if offset is not None:
            query += f" OFFSET {offset}"

        job_config = bigquery.QueryJobConfig()
        query_job = self.client.query(query, job_config=job_config)

        results = query_job.result()
        df = results.to_dataframe()

        posts = df.to_dict(orient='records')
        return posts