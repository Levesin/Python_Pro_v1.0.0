from application import fake_data


def main() -> None:
    num = 0
    while num == 0:
        try:
            num = int(input("Введите кол-во людей: "))
        except ValueError:
            print("Введите число! (0<) ")

        else:
            return fake_data(num)


if __name__ == "__main__":
    main()
