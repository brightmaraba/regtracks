from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_saver


app = Flask(__name__)

@app.route("/box-office-mojo-scraper", methods=['POST'])
def box_office_mojo_scraper():
    trigger_log_saver()
    scrape_runner()
    return {"Message":"Done"}
