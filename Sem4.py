'''
Мы, начиная с 1-го занятия, активно используем функции - например print.
Сегодня мы научимся создавать функции самостоятельно.
По своей сути функция - это часть программы, которая может выполняться
с разными параметрами и необходимость в исполнении которой возникает регулярно.
(вспомните print - мы регулярно испытываем необходимость вывести что-то - то число, то строку,
то результат каких-то наших действий - на консоль)

Когда нам понадобятся свои функции?
а) Когда какой-то кусочек (блок) программы нам надо будет выполнить несколько
раз (чтобы не прописывать его каждый раз полностью, а вместо этого вызывать функцию)
б) когда наша программа очень большая, мы можем какие-то ее части (блоки) оформлять
в виде функции, чтобы было легче разобраться в этой программе

Изучим создание функций на примере создания функции для подсчета факториала
Напомним, что факториал - это произведение первых n значений: 
4! = 1 * 2 * 3 * 4
'''

'''
сперва просто создадим код для расчета факториала любого числа n
'''

n = int(input())    #вводим целое число, факториал которого нам надо посчитать
fact = 1            #создаем переменную fact, которая будет равна факториалу заданного числа. На первом шаге присваем ей значение 1, потому что и 0! и 1! = 1 (это для случая если введем n = 0 или 1)
i = 2               #создаем цикл для расчета факториала
while i <= n:      
    fact *= i
    i += 1
print(fact)         #выводим рассчитанное значение факториала на консоль

'''
Теперь создадим функцию,куда вынесем расчет факториала
'''

def factorial(num):  #def - команда, определяющая функцию. В ней указываем имя определяемой функции (factorial) и в скобках имя ее параметра (num). В конце обязательно ставим двоеточие.
    fact = 1         #обратите внимание, что параметр в данном случае это "место" для ввода числа, чей факториал мы будем считать. Потом на "место" num  мы сможем вводить любое число, а сейчас нам надо описать, что с этим числом будет происходить в функции
    i = 2
    while i <= num:
        fact *= i
        i += 1
    return fact      #return это команда прекращения работы функции и возвращения ее параметра

n = int(input())     #вводим число, чей факториал мы хотим рассчитать
print(factorial(n))  #вызываем только что созданную функцию

'''
теперь с помощью созданной нами функции мы можем рассчитать значение 
суперфакториала - произведения первых n факториалов
'''

n = int(input())
superfact = 1
i = 2
while i <= n:
  superfact = superfact * factorial(i)
  i = i + 1
print(superfact)

'''суперфакториал 4 будет равен 288'''

''' Функции могут иметь много аргументов/параметров, и в качестве таковых
могут выступать константные значения (одно или несколько), переменные
(одна или несколько) и результаты вычисления арифметических
выражений и исполнения других функций
(вспомним все ту же функцию print, какие разные вещи мы записывали в ее аргумент)
'''
'''
Команда return, как мы помним, завершает исполнение функции, возвращая ее значение
Если у нас несколько аругментов, то мы можем прописать в команде return возвращение
нескольких значений, или каждого значения в каком-то своем месте функции - в зависимости от наших потребностей

Примеры:
Вычисление максимума:'''

def max2(a, b):
    if a > b:
        return a
    else:
        return b

'''
или
'''

def max2(a, b):
    if a > b:
        return a
    return b

''' или'''

def max3(a, b, c):
    return max2(max2(a, b), c)    
    

'''несколько значений'''

def sort2(a, b):
    if a < b:
        return a, b
    else:
        return b, a
a = int(input())
b = int(input())
minimum, maximum = sort2(a, b)
print(minimum, maximum)


''' Глобальные и локальные переменные
Если переменная задается вне тела функции - это глобальная переменная,
она "видна" и может использоваться в любом месте программного кода
Если же переменная задается внутри тела функции - это локальная переменная
которая существует только внутри функции
Сравним
'''
def f():
    print a
a = 1        #переменная а задана вне тела функции
f()

''' и '''
def f():
    a = 1    #переменная а задана в теле функции
f()
print(a)








команда возврата значения функции
