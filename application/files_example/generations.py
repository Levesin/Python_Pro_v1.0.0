from faker import Faker


def generate_user(q=100):
    fake = Faker()
    num = 0
    for _ in range(q):
        num += 1
        print(
            f"Номер:{num}\n"
            f"Имя: {fake.name()},\n",
            f"Email: {fake.email()},\n",
            f"{'-' * 30}")


def fake_data(num):
    fake = Faker()
    for index in range(1, num):
        print(
         f"Имя: {fake.name()},\n"
         f"Фамилия: {fake.address()},\n"
         f"Номер: {fake.phone_number()},\n"
         f"Email: {fake.email()},\n"
         f"{'-'*30}")


def create_txt():
    fake = Faker('ru_RU')
    return fake.text().replace(". ", ".\n")
