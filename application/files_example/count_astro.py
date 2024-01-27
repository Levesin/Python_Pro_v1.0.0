import json

from application.config.paths import FILES_OUTPUT_PATH


def number_of_astro(name_file: str = "output") -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{name_file}.json")
    with open(path_to_file) as file:
        response_dict = json.load(file)
    number_o_astro = response_dict["number"]
    answer = f"The number of people in space at this moment: {number_o_astro} astronauts"
    print(answer)


if __name__ == "__main__":
    number_of_astro()
