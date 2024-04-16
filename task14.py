array = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]
transponed = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
]
transponed[0][0], transponed[1][1], transponed[2][2], transponed[3][3], transponed[4][4] = array[0][0], array[1][1], array[2][2], array[3][3], array[4][4]
transponed[0][1], transponed[0][2], transponed[0][3], transponed[0][4] = array[1][0], array[2][0], array[3][0], array[4][0]
transponed[1][0], transponed[2][0], transponed[3][0], transponed[4][0] = array[0][1], array[0][2], array[0][3], array[0][4]
transponed[1][2], transponed[1][3], transponed[1][4] = array[2][1], array[3][1], array[4][1]
transponed[2][1], transponed[3][1], transponed[4][1] = array[1][2], array[1][3], array[1][4]
transponed[2][3], transponed[2][4] = array[3][2], array[4][2]
transponed[3][2], transponed[4][2] = array[2][3], array[2][4]
transponed[3][4] = array[4][3]
transponed[4][3] = array[3][4]
print('Исходная матрица:',
      '\n', array[0], '\n', array[1], '\n', array[2], '\n', array[3],
      '\n', array[4], '\n')
print('Транспонированная матрица:',
      '\n', transponed[0], '\n', transponed[1], '\n',
      transponed[2], '\n', transponed[3], '\n', transponed[4])