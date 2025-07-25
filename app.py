from src.mlproject.exception import CustomException
from src.mlproject.logger import logging


if __name__ == "__main__":
    try:
        print("hello world")
        logging.info(f"started execution")

    except Exception as e:
        raise CustomException(e)
