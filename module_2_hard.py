number = int(input('Введите число c каменной таблички: '))
while True:
    if number < 3 or number > 20:
        number = int(input('Вы ввели некорректное число, попробуйте ещё раз: '))
        continue
    else:
        key_ = []
        for i in range(1, number):
            for j in range(i, number + 1 - i):
                if i == j:
                    continue
                elif number % (i + j) == 0:
                    key_.append(i)
                    key_.append(j)
    key_ = str(key_)
    key_ = key_.replace('[', '').replace(']', '').replace(' ', '').replace(',', '')
    print('_________________________________________________________________')
    print(f'Введите следующий код: ', key_)
    print('_________________________________________________________________')
    answer_ = str((input('Дверь открыта? (Введите "Да", или продолжайте вводить числа): ')))
    if answer_ == 'Да'.casefold() or answer_ == 'lf'.casefold():
        print('Поздравляю! Надеюсь, вы не умерли пока я каждый раз задавал вам вопроос, открылась ли дверь =)')
        break
    elif answer_ == 'yes'.casefold() or answer_ == 'нуы'.casefold():
        print('Поздравляю, вы всё ещё живы! Надеюсь, вы не получили увечий пока я каждый раз задавал вопроос, открылась ли дверь =)')
        break
    else:
        number = int(answer_)
        continue