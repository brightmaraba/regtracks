from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_saver

app = FastAPI()

@app.post("/box-office-mojo-scraper")
def box_office_mojo_scraper_view():
    trigger_log_saver()
    scrape_runner()
    return {"message": "Done!"}