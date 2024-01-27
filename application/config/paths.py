from pathlib import Path
from typing import Final

ROOT_PATH: Final[Path] = Path(__file__).parents[2]
FILES_INPUT_PATH: Final[Path] = ROOT_PATH.joinpath("input_file")
FILES_OUTPUT_PATH: Final[Path] = ROOT_PATH.joinpath("output_file")
