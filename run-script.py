from app.services import get_data_from_website, store_posts_csv
from app.services import get_data_from_whois_api, etl_bigquery

# 1. Get data from website and store it in a CSV file
# posts = get_data_from_website()
# store_posts_csv(posts)

# 2. With the posts array already stored in the csv file, get the domain data from the whois api
# domain_data = get_data_from_whois_api(posts)

# 3. ETL process to load the data into BigQuery
etl_bigquery()