from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "hello world"

if __name__ == "__main__":
    try:
        app.run(debug=True, host="0.0.0.0", port=5000)
        logging.info(f"started execution")

    except Exception as e:
        raise CustomException(e)
