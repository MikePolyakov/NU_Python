"""
Просим пользователя ввести год рождения А.С. Пушкина до тех пор пока он не ввел правильный год,
после этого спрашиваем день рождения до тех пор, пока он не ввел верный день.
После верного ответа выводим в терминал 'Верно' и выходим из программы
"""
born_year = ''
while born_year != '1799':
    born_year = input('Напишите год рождения А.С.Пушкина. ')

born_day = ''
while born_day != '26':
    born_day = input('Напишите день рождения А.С.Пушкина. ')

print('Верно')