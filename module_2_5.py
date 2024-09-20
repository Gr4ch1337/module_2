def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for j in range(m):
            list_.append(value)
    return matrix
result_1 = get_matrix(2, 2, 'hello')
result_2 = get_matrix(6, 2, 'mr')
result_3 = get_matrix(1, 2, 77.3)
print(result_1)
print(result_2)
print(result_3)