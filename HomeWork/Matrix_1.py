# Входные данные
m = int(input('Enter M:'))
n = int(input('Enter N:'))

# Функция для создания матрицы
def make_matrix(m, n):
    # Пустая матрица
    matrix = []
    for i in range(m):
        # Создания пустой строки
        column = []
        for j in range(n):
            # Добавление элементов в строку
            column.append(0)
        # Печать для наглядного вида матрицы
        print(column)
        # Добавление строки в патрицу
        matrix.append(column)
    return matrix

# Создание матрицы
outputMatrix = make_matrix(m, n)

# Вывод матрицы
print(outputMatrix)