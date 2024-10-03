answer_year = True
while answer_year:
    pushkin_birth_age = input("Введите год рождения А.С. Пушкина: ")
    if pushkin_birth_age == "1799":
        answer_year = False

answer_day = True
while answer_day:
    pushkin_birth_day = input("Введите день рождения А.С.Пушкина: ")
    if pushkin_birth_day == "6":
        answer_day = False

print("Верно")
