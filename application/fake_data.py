from faker import Faker


def fake_data(num):
    fake = Faker()
    for index in range(1, num):
        print(
         f"Имя: {fake.name()},\n"
         f"Фамилия: {fake.address()},\n"
         f"Номер: {fake.phone_number()},\n"
         f"Email: {fake.email()},\n"
         f"{'-'*30}")




