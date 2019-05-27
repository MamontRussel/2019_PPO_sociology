'''
Недели 5-7 Сoursera.
Чтение файлов, множества, словари, обработка ошибок, дополнительные методы работы со строками.
'''

'''
МЕТОДЫ РАБОТЫ СО СПИСКАМИ
Списки в Python поддерживают множество методов для взаимодействия с ними. 
Стоит отметить, что эти методы изменяют исходный список.
'''

test_list = list(range(10))
print(test_list)

# Добавляет в список указанный элемент (в конец)
test_list.append(11)
print(test_list)

# Сформируем другой список
sublist = [12, 12]
# И добавим его в существующий (в конец)
test_list.extend(sublist)
print(test_list)

# Добавим в список строку "ABC" на позицию "1". Отличие от test_list[1] = 'ABC' в том, что сейчас элемент,
# стоявший под индексом 1 не перезапишется, а все элементы сдвинутся вправо.
test_list.insert(1, 'ABC')
print(test_list)

# Удалим из списка первое вхождение указанного элемента (по значению).
test_list.remove('ABC')
print(test_list)

# Найдём позицию указанного элемента в списке. Если элемент встречается несколько раз,
# то метод вернёт наименьшую позицию повторяющегося элемента.
print(test_list.index(12))

# Метод возвращает количество указанных элементов в списке
print(test_list.count(12))

# Метод возвращает элемент списка с указанным индексом и одновременно убирает его.
popped_element = test_list.pop(5)
print(popped_element)
print(test_list)

# Если индекс не указан - метод убирает последний элемент списка.
popped_element = test_list.pop()
print(popped_element)
print(test_list)

# Метод меняет порядок расположения элементов в списке на противоположный
test_list.reverse()
print(test_list)

'''
УПРАЖНЕНИЯ
1. Напишите програму, которая считает количество строк с длиной 4 или больше и в которых первый и последний символы
совпадают.
Sample List : ['abca', 'xydz', 'aba', '12321', 'dd']
Ожидаемый результат : 2

2. Напишите код, который удаляет дубликаты из списка.

3. Напишите функцию, которая сравнивает два списка и возвращает True, если у них есть хотя бы один общий член.

4. Напишите программу, которая удаляет все четные числа из списка.

5. Напишите программу, которая в каждом подлисте находит максмум и суммирует их.
'''
# 1
test_list = ['abca', 'xydz', 'aba', '12321', 'dd']
count = 0
for item in test_list:
    if (len(item) > 3) and (item[0] == item[-1]):
        count += 1
print(count)

# 2


def common_data(list1, list2):
    common = False
    for x in list1:  # итеририуемся по первому списку
        for y in list2:  # итерируемся по второму списку
            if x == y:
                common = True
                return common


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# 3
test_list = [2, 3, 6, 8, 19, 21, 22, 3, 3, 5, 20, 21]
new_list = []  # создаем пустой списко
for item in test_list:
    if item not in new_list:
        new_list.append(item)  # если элемент еще не в списке, то добавляем его
print(new_list)

# 4
test_list = [2, 3, 6, 8, 19, 21, 22]
new_list = []
for item in test_list:
    if item % 2 != 0:
        new_list.append(item)
print(new_list)

# 5
sum = 0
test_list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
for list in test_list:  # итерируемся по элементам большого списка
    max = 0
    for element in list:  # итерируемся по элементам каждого вложенного списка
        if element > max:
            max = element
    sum += max

print(sum)

'''
Отдельно следует рассказать про метод sort(). Метод производит сортировку списка.
Задачи сортировки - очень распространены в программировании. 
В общем случае, они сводятся к выстроению элементов списка в заданном порядке.
В Python есть встроенные методы для сортировки объектов для того, чтобы программист 
мог не усложнять себе задачу написанием алгоритма сортировки. 
Метод list.sort() - как раз, один из таких случаев.
'''

test_list = [5, 8, 1, 4, 3, 7, 2]
print(test_list)  # Элементы списка расположены в хаотичном порядке
test_list.sort()
print(test_list)  # Теперь элементы списка теперь расположены по возрастанию

'''
Таким образом, метод list.sort() упорядочил элементы списка test_list
Если нужно отсортировать элементы в обратном порядке, то можно использовать:
'''

test_list.sort(reverse=True)  # параметр reverse указывает на то, что нужно отсортировать список в обратном порядке
print(test_list)

'''
Следует обратить внимание, что метод list.sort() изменяет сам список, на котором его вызвали. 
Таким образом, при каждом вызове метода "sort()", наш список "test_list" изменяется. 
Это может быть удобно, если нам не нужно держать в памяти исходный список. 
Однако, в противном случае, или же - в случае неизменяемого типа данных (например, кортежа или строки) - 
этот метод не сработает. В таком случае, на помощь приходит встроенная в питон функция sorted()
'''

print(sorted(test_list))  # Сам список при сортировке не изменяется

'''
У функции sorted(), как и у метода list.sort() есть параметр key, 
с помощью которого можно указать функцию, которая будет применена к каждому элементу 
последовательности при сортировке.
'''
test_string = 'A string With upper AND lower cases'
print(sorted(test_string.split()))
print(sorted(test_string.split(), key=str.upper))

'''
Имеем строку из слов, начинающихся с заглавных и строчных букв. 
test_strng.split() формирует список из элементов строки, разделённых пробелом. 
Далее, функция "sorted()" уже сортирует этот список, меняя регистр всех входящих в него элементов на верхний.
'''

'''
ДОПОЛНИТЕЛЬНО
Однако, в некоторых случаях, встроенных функций Python для сортировки недостаточно, 
и нужно реалиовать алгоритм самим. Поэтому, рассмотрим сортировку подсчётом (без использования sorted())
Например, это эффективнее в случаях, когда в списке много однотипных значений и нам нужно узнать,
сколько раз встречается каждое
'''

marks = [1, 2, 2, 5, 7, 4, 2, 10, 7, 10]
# Создаём список, заполненный нулям длины, равной значению наибольшего элемента исходного списка + 1
# Потому что возможные значения от 0 до этого максимума (11 штук в данном случае).
cntMarks = [0] * 11
for mark in marks:  # проходим по каждому значению в исходном списке с оценками
    cntMarks[mark] += 1  # обновляем счетчик оценки в списке с нулями, если такой элемент встречается
print(cntMarks)
for nowMark in range(11):  # выводим результаты подсчета
    print((str(nowMark) + ' ') * cntMarks[nowMark], end=' ')


'''
МНОЖЕСТВА
Еще одна важная структура данных в python - множества. Если вы знакомы с логикой или теорией множеств,
то это собрания уникальных элементов. Главное отличие множеств - то, что элемент в них может встречаться только
один раз (в отличие от списков и кортежей).
Создаются фигурными скобками или функцией set().
Множества часто используются, когда нам нужен перечень уникальных элементов (например, чтобы проверить,
если в данных ответ с определенным значением). Это экономит память хранения такого списка.
Множества могут содержать объекты разных типов, но только неизменяемые (числа, строки).
'''

set1 = {1, 2, 2, 3, 4, 4, 4, 5}
print(set1)

'''
Множества можно сравнивать между собой. К традиционным операциям добавляются дополнительные.
'''

firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)  # Все элементы совпадают
print(firstSet != secondSet)  # Есть различные элементы
print(firstSet <= secondSet)  # Все элементы А входят в B
print(firstSet < secondSet)   # Все элементы А входят в Б и есть различные элементы

'''
Количество элементов можно так же узнать с помощью функции len()
'''

len(set1)

'''
Мы можем применять к множествам логические операции, чтобы смотреть имеют ли они общие или разные элементы.
'''

firstSet = {1, 2, 1, 3, 5, 9}
secondSet = {3, 2, 1, 4}
print(firstSet)
print(secondSet)
print(firstSet | secondSet)  # Объединение множеств
print(firstSet & secondSet)  # Пересечение множеств
print(firstSet - secondSet)  # Множество, элементы которого входят в A, но не входят в B
print(firstSet ^ secondSet)  # Элементы входят в A | B, но не входят в A & B

'''
Давайте теперь напишем программу, которая удаляет дубликаты из списка.
'''

test_list = [2, 3, 6, 8, 19, 21, 22, 3, 3, 5, 20, 21]
new_list = list(set(test_list))  # cоздаем множество из списка - дубликаты удаляются, делаем из множества список
print(new_list)

'''
СЛОВАРИ
Словарь - это такая структура данных, когда мы хотим хранить данные не по индексу, а чтобы какому-то
ключю соответствовало какое-то значение (например, как в телефонной книге). 
Ключом (именем в телефонной книге) может быть любой неизменяемый объект(число, строка), а значением - 
любой (в т.ч. список, словарь, кортеж).
Создать словарь можно с помощью фигурных скобок или функции dict(). Ниже обратите внимание на синтаксис.
'''

phone_book = {'Tanya': '243-352', 'Oleg': ['242-212', '242-251']}
print(phone_book)

'''
Словарь - неупорядоченная структура. Мы не можем обратиться к объекту по индексу, но зато можем по ключу.
'''

print(phone_book['Tanya'])

'''
Чтобы узнать, какие ключи (keys) или значения (values) есть в словаре - можно воспользоваться соответствующими
методами.
'''

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())  # возвращает объект с ключами и значениями, по которому можно итерироваться

'''
Мы можем вывести ключи и соответсвующие им значения с помощью цикла for
'''

for key in phone_book.keys():  # выведем все ключи
    print(key, phone_book[key])

for key, value in phone_book.items():  # выведем все пары ключ-значение
    print(key, value)

'''
Добавлять пары ключ значение в словарь очень просто: это делается по аналогии со списками.
Удаление происходит с помощью функции del.
Также можем проверить наличие ключа в словаре.
'''

phone_book['Alex'] = '242-325'
phone_book['Tanya'] = '25321-311'  # перезаписываем значение
print(phone_book)
del phone_book['Oleg']
print(phone_book)
print('Oleg' in phone_book.keys())

'''
Помните, мы сортировали список с оценками? Можем собрать два списка в словарь, где ключ - оценка,
а значение - сколько раз она встречается в списке.
'''
print(marks)
print(cntMarks)
marksDict = dict(zip(range(11), cntMarks))
# смотрит, что делает функция zip - она упаковывает два списка одинаковой длины попарно в кортежи
# первый объект с первым и так далее. Функция dict() в свою очередь, может распаковать такую структуру
# в словарь
print(list(zip(range(11), cntMarks)))
print(marksDict)

'''
Напишите программу, которая объединяет значения из двух списков.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
'''

sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
new_dictionary = {}  # создаем пустой словарь
for dictionary in sample_data:  # итерируемся по списку - заходим в каждый вложенный словарь
    if dictionary['item'] in new_dictionary.keys():  # проверяем, есть ли в нашем новом словаре такой ключ
        # если такой ключ там есть, то обновляем его значение
        new_dictionary[dictionary['item']] = new_dictionary[dictionary['item']] + dictionary['amount']
    else:
        # если такого ключа нет - создаем его и присваиваем ему соответствующее значение
        new_dictionary[dictionary['item']] = dictionary['amount']
print(new_dictionary)

'''
Вариант условия этой задачи для практики.
У вас есть выгрузка оставшегося количества фруктов из базы данных магазинов. Каждый словарь в списке - магазин.
Какие-то фрукты есть в разных магазинах, какие-то только в одном. Нужно сделать словарь, в котором ключами 
будут фрукты, а их количество - значениями. Если фрукт есть в наличии в нескольких магазинах - 
сложите эти значения. 

Ввод:
[{'фрукт': 'банан', 'количество': 400}, {'фрукт': 'яблоко', 'количество': 300}, 
{'фрукт': 'банан', 'количество': 750}, {'фрукт' : 'груша', 'количество' : 20}, {'фрукт': 'яблоко', 'количество': 150}]

Вывод: фрукты и их общее количество, список упорядочен по алфавиту.

банан 1150
груша 20
яблоко 450
'''


'''
Словари очень удобно использовать для подсчета числа элементов.
Давайте попробуем открыть файл и решить небольшую задачку.
Мы открываем файл с помощью функции open(), которой передаем адрес файла, 
форму работы с файлом (только чтение r, запись w, запись и чтение r+) и кодировку
(utf8 в нашем случае). Этот файл загружается в память.
Затем мы можем загружать его по строкам.
Обратите внимание, что файл нужно положить в папку вышего проекта, если вы не хотите прописывать
к нему полный путь.
'''

file = open('romeo.txt', 'r', encoding='utf8')  # загружаем файл в память
lines = file.readlines()  # создаем объект, который при каждом обращении будет загружать новую строку в память

for line in lines:
    print(line)


'''
Давайте посчитаем, какие слова и как часто встрачаются в нашем файле. 
Создадим словарь, в котором ключом будет слово, а значением - количество раз, которое оно встречается.
'''
file = open('romeo.txt', 'r', encoding='utf8')  # загружаем файл в память
lines = file.readlines()  # перезаписываем объект lines, потому что выше итератор дошел до конца и закончился
words = dict()  # создаем пустой словарь
for line in lines:  # итерируемся по строкам файла
    templst = list(map(lambda x: x.lower(), line.split()))  # cохраняем все слова из строки в список в нижнем регистре
    print(templst)
    for word in templst:  # итерируемся по списку, созданному на основе строки
        if word in words.keys():  # проверяем наличие ключа в словаре
            words[word] += 1      # если ключ в словаре - прибавляем 1
        else:
            words[word] = 1       # если такого ключа нет - сохраняем ключ со значением один
        print(word, words[word])

print(words)
print(words['pale'])

'''
Теперь давайте найдем самое часто встречающееся слово. К сожалению словарь неупорядоченная структура данных
и нам придется отсортировать его в ручную. Сделаем этот код функцией, потому что он нам пригодится в следующей задаче.
'''
def dict_max_value(x):
    # будем считать, что по умолчанию максимульное значение равно одному, потому что в наших словарях
    # каждое слово встречается минимум 1 раз
    max_value = 1
    # значение максимальное ключа мы пока не знаем, поэтому создаем пустую переменную
    max_key = None
    for key, value in x.items():  # итерируемся по парам ключ-значение
        if value > max_value:  # проверяем, больше ли значение, чем максимум
            max_key = key  # обновляем ключ, если да
            max_value = value  # обновляем значение
    if max_value == 1:  # если нет ни одного значения больше одного, давайте выведем эту информацию
        print('No max value, all 1')
    else:
        print('Max value is', max_value, 'for', max_key)

dict_max_value(words)

'''
ЗАДАЧА НА АВТОРА, КОТОРЫЙ ПИШЕТ БОЛЬШЕ ВСЕГО ПИСЕМ.
Файл mbox.txt содержит метаданные почтового сервера.
Мы знаем, что строка с адресом автора письма начинается с "From " (посмотрите в самом файле,
какие там еще есть варианты). Мы хотим найти адреса всех авторов сообщений и найти того из них, кто пишет
больше всех писем.
'''

handle = open('mbox.txt', 'r', encoding='utf8')
emails = {}
for line in handle:
    if line.startswith('From '):   # работаем только со строками, которые нас интересуют
        email = line.split()[1]  # разбиваем строку и берем из нее email
        if email not in emails.keys():  # проверяем, есть ли уже такой адрес в нашем словаре
            emails[email] = 1  # если нет, то создаем такой ключ со значением 1
        else:
            emails[email] += 1  # если да, то обновляем значение на 1
print(emails)

dict_max_value(emails)  # воспользуемся нашей функцией, чтобы найти максимальное значение

'''
ЗАДАЧА НА ПАРСИНГ ДАННЫХ
В том же файле есть строка, которая обозначает, насколько спам фильтр уверен, что данное письмо не спам.
Давайте найдем среднее значение X-DSPAM-Confidence для всей переписки.
Нас интересуют только строки, начинающиеся с 'X-DSPAM-Confidence: '
(посмотрите в файле структуру метаданных хотя бы одного письма).
'''

fhand = open('mbox.txt', 'r', encoding='utf8')
count = 0  # создаем счетчик писем
total = 0  # cоздаем переменную, в которой будем обновлять суммарное значение X-DSPAM-Confidence
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):  # работаем только с интересующим нас строками
        print(line)
        x = line.find(':')  # ищем местоположение символа, по которому будем срезать строку
        confidence = line[x+2:x+7]  # ищем индексы, по которым будем доставать значение X-DSPAM-Confidence
        y = float(confidence)  # переводим значение из строки в дробь
        print(y)
        count = count + 1  # обновляем count
        total = total + y  # обновляем total
average = total/count  # находим среднее
print('Average spam confidence: ', round(average, 2))



'''
МЕТОДЫ ДЛЯ РАБОТЫ СО СТРОКАМИ
Словари очень часто используются для работы с текстом, поэтому давайте посмотрим, 
какие еще методы для строк есть в Python.
'''

# isalpha - проверяет, что все символы строки являются буквами.
print('Ask me a question!'.isalpha())
print('Ask'.isalpha())

# isdigit - проверяет, что все символы строки являются цифрами.
print('13242'.isdigit())

# isalnum - проверяет, что все символы строки являются буквами или цифрами.
print('Ask me a question!'.isalnum())
print('Ask232'.isalnum())

# islower - проверяет, что все символы строки являются маленькими (строчными) буквами.
print('ssk me a question!'.islower())

# isupper - проверяет, что все символы строки являются большими (заглавными, прописными) буквами.
print('ssk me a question!'.isupper())

# lstrip - обрезает все пробельные символы в начале строки.
print(' ssk me a question! ')
print(' ssk me a question! '.lstrip())

# rstrip - обрезает все пробельные символы в конце строки.
print(' ssk me a question! '.rstrip())

# strip - обрезает все пробельные символы в начале и конце строки.
print(' ssk me a question! '.strip())

