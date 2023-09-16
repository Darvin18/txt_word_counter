**<h1><span style="color: #ea4357">Счётчик слов в файле</span></h1>**
<h2><span style="color: #ea4357">Программа умеет:</h2>
<h4>1. Считать ОБЩЕЕ количество слов в файле (команда: слова)
<br>2. Считать, сколько раз в файле встретилось выбранное вами слово (команда: слово)
<br>3. Чтобы выйти, используйте команду: exit</h4>

**<h2><span style="color: #65fc00">Функция, показывающая: сколько раз в файле встретилось выбранное вами слово</h2>**
```python
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
```

**<h2><span style="color: #65fc00">Функция подсчёта общего количества слов в файле**</h2>
```python
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
```
# <span style="color: #ea4357">Примечание!
<h3><span style="color: #ea4357">На винде путь к файлу нужно указывать в формате: E:/flower_photos/LICENSE.txt</h3>