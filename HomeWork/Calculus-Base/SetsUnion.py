# Импорт randint из библиотки random
from random import randint

# Длинна множества а, счетчик и создание множества а
num = int(input('Количество элементов в вашем множестве: '))
count = 0
a = set()

# Заполнение множества а, в данном примере множество заполняеться только цифрами для нагладности обьединения множеств
while count != num:
    a.add(int(input('Добавить элемент: ')))
    count += 1

# Множество b
b = {randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)}

# Обьединение множеств
print(a | b)
