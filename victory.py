persons = [['А. С. Пушкина', '1799'],#1799
           ['В. И. Ленина', '1870'],#1870
           ['Петра 1', '1672'],#1672
           ['Д. И. Менделеева', '1834'],#1834
           ['Ю. А. Гагарина', '1934']]#1934
correct_answer_count = 0
for person in persons:
    birth_age = input("Введите год рождения {}: ".format(person[0]))
    if birth_age == person[1]:
        correct_answer_count += 1

print("Количество правильных ответов: {}".format(correct_answer_count))
print("Количество ошибок: {}".format(5-correct_answer_count))
print("Процент правильных ответов : {}".format(100*correct_answer_count/5))
print("Процент неправильных ответов: {}".format(100*(5-correct_answer_count)/5))

