matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# print(matriz[2][4])

for i in range(len(matriz)):
    print(matriz[i])

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j])
