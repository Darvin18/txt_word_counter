func = []

def f_slovo(filename, slovo):
    try:
        with open(filename, encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print('Файла нету в указанной директории!')
        func.clear()
    else:
        slova = text.lower().count(slovo)
        print(f'Количество слова: {slovo} в файле: {slova}')

def f_slova(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print('Файла нету в указанной директории!')
        func.clear()
    else:
        count_slova = text.split()
        print(f'Общее количество слов в файле: {len(count_slova)}')

while True:
    print('Программа умеет: \n1.Считать ОБЩЕЕ количество слов в файле (команда: слова)\n2.Считать,'
          'сколько раз в файле встретилось выбранное вами слово (команда: слово)\nЧтобы выйти, используйте команду: exit')
    a = input('Для выбора введите: слово / слова / exit:')
    if a == 'exit':
        print('Вы вышли из программы')
        break
    
    elif a == 'слова' or a == ' слова':
        while True:
            first_quest = input('Введите название файла: ')
            if first_quest == 'exit':
                print('Вы вернулись на шаг назад\n')
                break
            func.append(first_quest)
            for i in func:
                f_slova(i)
                func.clear()
                
    elif a == 'слово' or a == ' слово':
        while True:
            quest = input('Введите название файла: ')
            second_question = input('какое именно слово вы хотите найти в файле: ')
            if quest == 'exit' or second_question == 'exit':
                print('Вы вернулись на шаг назад')
                break
            func.append(quest)
            for i in func:
                f_slovo(i, second_question)
                func.clear()
