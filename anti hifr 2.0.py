u = input('input:')#ввод от пользователя
ug = 'orange'#1 ключ
h1 = 'itre'#2 ключ
h2 = 580#3 ключ
h3 = 'L'#4 ключ
h4 = 70#5 ключ
h = len(h1)#количество символов во 2 ключе
ee1 = ord(h3)
e1 = 870
o=0#число символа слова введёного пользавателем
ug1 = len(ug)#количество символов 1 ключа
u1 = len(u)#количество букв слова пользавателя
y = ''#пустая строка
f = u[o]#определение цифры слова пользавателя
jk = ''#пустая строка
print('log:')
while o<=u1:#цикл
    if o==u1:
        break
    else:
        f = u[o]
        y = ord(f)
        y1 = y-e1
        print(y1)
        y1 = y1+ee1
        print(y1)
        y1 = y1/h
        print(y1)
        y1 = y1+h4
        print(y1)
        y1 = y1-ee1
        print(y1)
        y1 = y1+h2
        print(y1)
        y1 = y1/ug1
        print(y1)
        y1 = y1-h
        print(y1)
        y1 = y1+ug1
        print(y1)
        jb = int(y1)
        ft = chr(jb)#
        print(ft)#
        jk = jk+ft#
        o=o+1#

print('output:')#вывод
print(jk)#то что получается при выводе
