answer = True
while answer:
    pushkin_birth_age = input("Введите год рождения А.С. Пушкина: ")
    if pushkin_birth_age == "1799":
        print("Верно")
        answer = False
    else:
        print("Неверно")
