def num1(x):
    print('Первое задание\n')
    print('Ввод',x)
    l=[]
    while x > 0:
        l.append(x % 10)
        x = x // 10
    for i in range(int(len(l) / 2)):
        if l[i] != l[len(l) - 1 - i]:
            return False
    return True
print('Вывод',num1(123321))
print()

def num2(x):
    print('Второе задание\n')
    print('Ввод', x)
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(len(x)):
        if x[i] % 2 == 0:
            a.append(x[i])
        if x[i] % 3 == 0:
            b.append(x[i])
        if x[i] % 5 == 0:
            c.append(x[i])
    d.append(a), d.append(b), d.append(c)
    print('Вывод',d)
    return 1
input = num2([1,2,3,4,5,6,7,8,9,10])
print()

def num5(x):
    print('Пятое задание\n')
    print('Ввод',x)
    for i in range(2, int(x / 2)):
        if x % i == 0:
            return False
    return True
print('Вывод',num5(7))
print()

def num3(x):
    print('Третье задание\n')
    print('Ввод', x)
    rev = int(str(x)[::-1])
    print('Вывод',rev)
input = num3(45678)
print()


def num4(x):
    print('Четвертое задание\n')
    print('Ввод',x)
    for i in range(1, x - 1):
        res = ((i ** 2 + x) / i) / 2
        # print (res)
        if (round(res ** 2) == x):
            print('Вывод', res)
input = num4(139)




