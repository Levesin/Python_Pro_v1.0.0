from application.files_example.generations import fake_data, create_txt, generate_user
from application.files_example.create_txt_file import create_txt_file
from application.files_example.read_txt import read_text_file
from application.logging.init_logging import init_logging
from application.files_example.count_astro import number_of_astro
from application.files_example.request_end_download import get_requests_data


def main() -> None:
    print("___________Меню___________")
    print("1.Создание фейковой базы данных")
    print("2.Считывание файла")
    print("3.Генератор пользователей")
    print("4.Кол-во космонавтов")
    number_menu = 0
    while number_menu == 0:
        try:
            number_menu = int(input("Выберите номер задания: "))
        except ValueError:
            print("Введите число! (0<) ")
        else:
            if number_menu == 1:
                num = 0
                while num == 0:
                    try:
                        num = int(input("Введите кол-во людей:"))
                        print("-"*30)
                    except ValueError:
                        print("Введите число! (0<) ")
                    else:
                        return fake_data(num)
            elif number_menu == 2:
                create_txt()
                create_txt_file()
                read_text_file()

            elif number_menu == 3:
                print("По умолчанию 100 пользователей\n"
                      "Можно задать параметр до 100")

                try:
                    question = int(input("Ожидается число: "))
                    print('-'*30)
                    generate_user(question)
                except ValueError:
                    generate_user()
            elif number_menu == 4:
                get_requests_data(url="http://api.open-notify.org/astros.json")
                number_of_astro(name_file="output")


if __name__ == "__main__":
    init_logging()
    main()
