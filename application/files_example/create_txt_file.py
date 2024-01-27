from application.config.paths import FILES_INPUT_PATH
from application.files_example.generations import create_txt
from application.logging.loggers import get_core_logger


def create_txt_file(name_file: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{name_file}.txt")
    with open(path_to_file, mode="w") as file:
        file.write(f"{create_txt()}")
    logger.info(f"Path to file: {path_to_file}")
