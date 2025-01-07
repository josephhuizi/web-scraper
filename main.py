from fastapi import FastAPI

from app.routers import data_router
from app.services import *

app = FastAPI()
app.include_router(data_router)

@app.get("/health-check")
async def root():
    return {"message": "The Web Scraper API is working properly!"}

def main():
    print("Hello from web-scraping-interview!")


if __name__ == "__main__":
    main()
