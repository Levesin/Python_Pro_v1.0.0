import json
import requests
from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger


def get_requests_data(url: str = None) -> None:
    logger = get_core_logger()
    path = FILES_OUTPUT_PATH.joinpath("output.json")
    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response}")
        response_json = response.json()
        path.write_text(json.dumps(response_json, indent=2))
        logger.info(f"Path to file: {path}")
