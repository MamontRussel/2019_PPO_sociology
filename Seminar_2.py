'''
Социология | 1 курс | ППО Data Culture | Семинар 2

На прошлом семинаре мы познакомились с условиями. 
Давайте вспомним, что это такое, разобрав еще несколько примеров работы с ними.
'''

'''
Пусть мы хотим найти максимум из двух чисел.
'''
a = 3
b = 5
max = a # изначально будем считать, что максимум - первое число. 
if b > a: # выше мы написали, что a = 3, a b = 5, то есть логическое выражение равно True, поэтому следующая строка кода выполнится
	max = b
print(max) # теперь максимум равен 5, что верно
'''
Что произойдет, если мы поменяем местами значения чисел?
'''
a = 5
b = 3
max = a
if b > a: # теперь выражение ложно, и следующая строчка кода не будет выполняться
	max = b
print(max) # максимум снова равен 5
'''
Эту же задачу мы может решить с использованием else
В предыдущем примере мы изначально сделали максимум равным первому числу, а потом проверяли, нужно ли сделать его равным второму числу.
Но мы можем поступить иначе и сказать: "Если первое число больше, то максимум равен первому, а ИНАЧЕ он равен второму".
'''
a = 3
b = 5
if a > b: # логическое выражение ложно
	max = a # поэтому эта строка кода выполняться не будет
else:
	max = b # зато будет выполняться эта
print(max) # и максимум все еще равен 5
'''
Например, в предыдущей задаче, если числа равны, мы хотим вывести слова 'Equal numbers'.
То есть у нас есть три варианта действий: напечатать первое число, напечатать второе число или напечатать слова 'Equal numbers'.
'''
a = 5
b = 5
if a > b: 
	print(a)
else:
	if a < b: # обратите внимание, здесь одно условие находится внутри другого, и код ниже будет писаться после двойного отступа
		print(b)
	else:
		print('Equal numbers')
'''
А теперь напишем то же самое с использованием elif.
'''
a = 5
b = 5
if a > b: 
	print(a)
elif a < b: 
	print(b)
else:
	print('Equal numbers')
'''
Одно условие можно вставлять внутрь другого, главное при этом не запутаться
'''
num = int(input())

if num > 100:
    if num < 150:
        print("Число больше ста, но меньше ста пятидесяти")
    elif num < 200:
        print("Число больше ста, но меньше двухсот")
elif num > 50:
    if num < 90:
        print("Число больше пятидесяти, но меньше девяноста")
    else:
        print("Число больше пятидесяти и больше девяноста")
else:
    print("Число меньше пятидесяти")

'''
Довольно часто задачи требуют от нас несколько раз выполнить однотипный код.
Если писать несколько раз одни и те же строки, это загромождает код 
А иногда несколько раз превращается в много (100 или 10000). Либо же это число вообще зависит от параметров ввода.
Справиться с этим помогают ЦИКЛЫ. На этом семинаре мы поработаем с циклом WHILE (пока)
'''
'''
Чтобы использовать цикл WHILE, нужно записать логическое выражение и некоторый код. 
И этот код будет выполняться до тех пор, пока логическое выражение верно.
'''
'''
Пусть мы хотим напечатать все целые числа от 1 до 100.
'''
i = 1 
while i <= 100:
	print(i) # код, который мы хотим неоднократно выполнить (код внутри цикла) пишется после отступа
	i += 1 # запись, эквивалентная i = i + 1. Аналогично можно записывать и другие арифметические операции.
'''
Пока логическое выражение, записанное после while, было верным (переменная i была не больше 100), мы выводили i и снова увеличивали.
Так продолжалось, пока i не стало равным 101 и логическое выражение стало ложным.
После этого начнет выполняться код, записанный после цикла (а в нашем случае программа завершится).
'''
'''
Циклами можно управлять с помощью операторов break, continue.
'''
'''
BREAK внутри цикла позволяет прервать его выполнение и сразу же перейти к коду, который идет после цикла (либо завершить программу).
В этом случае мы можем написать сразу после цикла секцию ELSE (синтаксис при этом такой же, как и в условиях).
Код, написанный после else, будет выполняться, если цикл завершился "естественным путем" (т.е. не был прерван с помощью break).
'''
'''
Рассмотрим пример использования break. Пусть студент сдал 5 предметов во время сессии и мы хотим узнать, есть ли у него пересдачи.
Ввод - до пяти оценок от 1 до 10. Если хотя бы одна из них меньше 4, завершаем программу и печатаем 'YES' (пересдачи есть).
Если все пять оценок больше 3, печатаем 'NO' (студент закрыл сессию без пересдач).
'''
i = 1
while i <= 5:
	note = int(input())
	if note < 4:
		print('YES')
		break
	i += 1
else: # else находится на том же уровне отступа, что и while, поэтому относится именно к циклу, а не к условию внутри цикла
	print ('NO')
'''
Оператор CONTINUE позволяет сразу же перейти на новую итерацию цикла, не выполняя код, который написан внутри цикла ниже его.
'''
'''
Пусть теперь мы хотим почитать количество пересдач у студента.
'''
i = 1
retakes = 0
while i <= 5:
	note = int(input())
	i += 1
	if note >= 4: # если пересдачи нет, сразу же идем проверять переменную i, без увеличесния переменной retakes
		continue
	retakes += 1
print(retakes)
'''
Операторами break и continue не стоит злоупотреблять, это значительно ухудшает читаемость кода.
Например, в предыдущем примере мы бы справились и без continue.
'''
i = 1
retakes = 0
while i <= 5:
	note = int(input())
	i += 1
	if note < 4:
		retakes += 1
print(retakes)
'''
Разберем более сложную задачу.

КОЛИЧЕСТВО ПАЛИНДРОМОВ

Назовем число палиндромом, если оно не меняется при перестановке его цифр в обратном порядке. 
Напишите программу, которая по заданному числу K выводит количество натуральных палиндромов, не превосходящих K.

Формат ввода
Задано единственное число K (1 ≤ K ≤ 100 000).

Формат вывода
Необходимо вывести количество натуральных палиндромов, не превосходящих K.

Пример
Ввод
10
Вывод
9
'''
'''
ИДЕЯ РЕШЕНИЯ

Заведем переменную, которая будет хранить количество палиндромов.
Будем перебирать все числа от одного до K и для каждого проверять, палиндром ли оно.
Проверку будем осуществлять, строя для числа его перевернутую версию и затем сравнивая ее с оригинальной.
Строить перевертыш будем так: стираем одну цифру из переворачиваемого числа и приписываем ее к перевернутому.
И повторяем это действие, пока переворачиваемое число не исчезнет, то есть не станет равным нулю.
'''
K = int(input()) # вводим исходное число
palindromes = 0 # здесь будем хранить количество палиндромов, изначально оно равно нулю
index = 1 # в этой переменной будет храниться число, которое мы в данный момент проверяем на "палиндромность"
while index <= K: # согласно условию задачи, палиндромы могут быть в диапазоне от 1 до K
    reverse = 0 # здесь будет храниться перевернутое число
    tmpIndex = index # создаем копию проверяемого числа, так как сейчас мы будем его "ломать", отбрасывая по одной цифре с конца
    while tmpIndex: # цикл перестанет работать, когда число будет равно 0, т.е. отбрасывать будет нечего
        lastNumber = tmpIndex % 10 # цифра, которую хотим переписать в перевернутое число
        reverse = reverse * 10 + lastNumber # сдвинули предыдущие цифры ближе к началу и поставили в конец то, что откусили
        tmpIndex = tmpIndex // 10 # отбросили последнюю цифру
    # например, хотим перевернуть число 692. тогда tmpIndex и reverse по ходу работы цикла будут равны 0 и 692, 2 и 69, 29 и 6, 296 и 0
    if index == reverse: # проверяем, что число палиндром. Здесь нам пригодилось то, что мы создали копию index
        palindromes += 1
    index += 1 # не забываем увеличить index
print(palindromes)