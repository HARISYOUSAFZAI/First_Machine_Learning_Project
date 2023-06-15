from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    logging.info("We are testing logging file")
    return "Starting Maching Learning Project"

if __name__ == "__main__":
    app.run(debug=True)