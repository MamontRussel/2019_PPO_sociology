# -*- coding: utf-8 -*-
"""Test1_183-184_Solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZS2VGRbErCwLuy6XGq-cf_7e5GdhngHH

# Самостоятельная №1

**Списывание и использование телефонов**

Первое предупреждение, сделанное ассистентом или преподавателем: - 1 балл к вашей оценке. 

Второе предупреждение: работа аннулируется без права переписывания.

0. **Оформление и стиль (0.5 балла).**

Этот балл у вас есть по умолчанию при условии сданной работы с решенными задачами. 

За каждый тип повторяющейся стилистической ошибки снимается 0.25 балла Повторяющейся считаем ошибку, допущенную минимум 2 раза.

0.25 балла снимается за каждые 4 не систематические ошибки (4 разных ошибки, допущенных по одному разу.)

Все задачи должны принимать значения на ввод (решение для частного случая будет считаться неполным).

1. **Тест (1 балл) Каждый вопрос 0.1 балла**
        1. В строке 'x = 24', x - это пример чего?
        2. print('This is word') - что здесь является аргументом функции?
        3. Как выглядит знак остатка от деления в Python?
        4. Как называется гид по стилю Python?
        5. Что будет результатом исполнения такого когда: print('14' + "6")?
        6. Что будет результатом выполнения такого кода: print('bana'+ 'na' * 3)?
        7. Что из ниже перечисленного является правильным написанием логической переменной “ложь” в Python?
            a. FALSE
            b. False
            c. false
        8. Как вызвать справочную информацию о функции?
        9.  9. Дан следующий код: 
            x = 7
            y = 15
            x = y + x
            y = x + 2
            print(y)
            
            Что будет выведено в консоль?

        10. Что будет результатом исполнения это кода: print(‘Hello, world”)
            a. Ошибка
            b. Hello, world
            c. ‘Hello, world”

**Здесь нужно написать ответ на задание №1**
"""

'''
Напишите в комментариях ответы. Одна строка - один ответ.
1. переменная
2. 'This is word'
3. %
4. PEP8
5. 146
6. banananana
7. b
8. help()
9. 24
10. a
'''

"""2. **(1 балл) Сколько дней в месяце?**

(1 балл) Оценка по 5-ти бальной шкале?
Напишите программу, которая переводит оценку из 10-ти бальной шкалы в 5-ти бальную. ("Отлично": от 8 до 10, "Хорошо": от 6 до 7, "Удовлетворительно": от 4 до 5, "Неудовлетворительно": от 0 до 3)

**Ввод программы:** целое положительное число. 

**Вывод программы:** вывести слово описывающее значение оценки. Если ввод некорректный, напечатать “Wrong input.”.
"""

# здесь нужно написать решение задачи №2
mark = int(input())
if 8 <= mark <= 10: 
    print('Отлично')
elif 6 <= mark < 8: # для проверки если mark будет float а не только int
    print('Хорошо')
elif 4 <= mark < 6:
    print('Удовлетворительно')
elif 0 <= mark < 4:
    print('Неудовлетворительно')
else: # необходимо во всех if захватить область от 0-10 все остальные значения wrong
    print('Wrong input.')

"""3. **(1,5 балла) Приемная комиссия** ПОМЕНЯТЬ

Результаты экзамена IELTS по английскому языку измеряются по шкале от 1.0 до 9.0 в каждой из четырех частей (speaking, reading, listening, writing). Чтобы поступить в магистратуру по социологии в Лондон, нужно получить общую оценку за экзамен не ниже 7.0, при этом не ниже 7.5  за Writing и не ниже 6.0 за любую из оставшихся частей. Общая оценка считается как среднее арифметическое (складываем оценки за четыре части и делим на 4). Напишите программу, которая принимает четыре оценки за четыре части экзамена и выдает YES, если документы можно подать и NO, если нет. Округлять дроби не нужно.

**Ввод:** четыре числа от 1.0 до 9.0  - баллы за Speaking, Reading, Listening и Writing.
**Вывод:** 
YES, если документы подать можно  
NO, если документы подать нельзя
"""

# здесь нужно написать решение задачи №3
s = float(input()) # если вы решили эту задачу с int() - мы не снижали оценки, но так - правильнее
r = float(input()) 
l = float(input())
w = float(input())
# здесь главное не делить нацело (//), 
# нам повезло что "нужно получить общую оценку за экзамен не ниже 7.0", 
# ведь если было бы допустим 7.5, а average = 7.6, деление нацело привело бы это среднее значение к 7.0
# и if не сработал бы, хотя 7.6 > 7.5
average = (s + r + l + w) / 4
# здесь главное захватить все условия в and ведь они должны выполняться все
# "не ниже" значит >=
if (average >= 7.0) and (w >= 7.5) and (s >= 6.0) and (r >= 6.0) and (l >= 6.0):
    print('YES')
else:
    print('NO')

"""4. **(0.5 балла) Привет, Петя!**

Напишите программу, которая приветствует пользователя.

**Ввод: **Имя пользователя name.

**Вывод: **"Привет, name!"

**Пример**
Ввод: Петя
Вывод: Привет, Петя!
"""

# Варианты решения
name = input()
print('Привет, ' + name + "!")
print('Привет, ', name, "!", sep='')
print('Привет,', name, end='!')

"""5. **(2,5 балла) Треугольник**

Напишите код, который определяет, можно ли построить треугольник с заданными длинами сторон. Для этого воспользуйтесь неравенством треугольника: любая сторона треугольника не превосходит суммы двух других (a <= b + c)

Подсказка: неравенство должно выполняться для каждой стороны

**Ввод: ** три числа от 1 до 100 - стороны треугольников.

**Вывод: ** YES, если можно постороить треугольник NO, если нельзя построить треугольник
"""

# здесь нужно написать решение задачи №5
a = int(input())
b = int(input())
c = int(input())
# здесь обязательно чтобы все стороны треугольника были меньше суммы других (иначе не треугольник)
if (a + b >= c) and (a + c >= b) and (c + b >= a):
    print ('YES')
else:
    print('NO')

"""6. **(1 балл) Конвертер валют** 

Курс евро 72 рубля 69 копеек  
Пусть у нас есть N евро. Сколько это будет в рублях?  

**Ввод:** два целых числа, количество евро и количество центов  
**Вывод:** два целых числа, количество рублей и копеек
"""

# здесь нужно написать решение задачи №6
# Ввод: ДВА целых числа, количество евро и количество центов
euro = int(input())
cent = int(input())
c = 72.69 #курс
mon = euro + cent/100 # кол-во денег в евро
rubs = mon * c # кол-во денег в рублях
# Вывод: ДВА ЦЕЛЫХ числа, количество рублей и копеек
# int действует как floor()
print(int(rubs), int(rubs*100%100)) # умножаем на 100 чтобы получить в копейках
print(rubs//1, rubs*100%100//1) # в принципе деление нацело выдает целое число (хоть и float) - это не считали ошибкой

"""**7. (2 балла) Разность суммы цифр**

Вводится целое неотрицательное число в десятичной записи. Посчитайте разность сумм его цифр, находящихся на четной позиции (второй, четвертой и так далее) и нечетной. (нечет - чет)

**Пример 1**  
**Ввод:**  
3456  
**Вывод:**  
-2  

**Пример 2**  
**Ввод:**  
1  
**Ввод:**  
1  

**Пример 3**  
**Ввод:**  
12  
**Ввод:**  
-1
"""

# сюда нужно вставить решение задачи №6
# дополненное решение студента
x = int(input())
a = 0 # сумма №1
b = 0 # сумма №2
k = 1
while x != 0:
    # здесь цикл проходится по 2 цифре с конца
    # в задании начало нечетных берется слева
    # суммы a,b берутся справа поэтому нельзя сказать точно что одна из них чет или нечет
    # поэтому можно сделать чтото вроде переключателя 1,-1
    # при четных порядках числа k=1, при нечетных k=-1
    if ((x % 10 != 0) and ((x % 100) // 10 == 0)):
        k = -1
    a = a + (x % 10) # добавляем к первой сумме последнюю цифру
    b = b + (x % 100 // 10) # добавляем ко второй сумме предпоследнюю цифру
    x = x // 100 # убираем последние 2 цифры
print (k*(b - a))

x = int(input())
summa1 = 0
summa2 = 0
k = 1
i = -1
# цикл проходится по 1 цифре с конца
while x != 0:
    cur = x % 10
    if i == 1:
        summa1 = summa1 + cur
    else:
        summa2 = summa2 + cur
    x = x // 10 # убираем последнюю цифру
    i = i * (-1)
print(i*(summa2 - summa1))

"""#####"""

# решения строками
x = input() # на всякий случай указали явно строковый тип
c = 0 # индекс цифры в числе
sum = 0 # итоговая сумма
while c != len(x): # перебираем все цифры в числе
  if c % 2 == 0: # если индекс цифры нечетный, то добавляем число. ВНИМАНИЕ! Т.к. отчет идет с 0, то проверка на четной\нечетность инвертируется: 0,2,4,6 - нечетные индексы; 1,3,5 - четные индексы
    sum = sum + int(x[c])
  else: # если четный, то отнимаем
    sum = sum - int(x[c])  
  c = c + 1
print(sum)

