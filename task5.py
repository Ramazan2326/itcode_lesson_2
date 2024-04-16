stroke = str(input('Введите строку, состоящую из двух слов, разделенных'
                   ' пробелом: ')).split()
stroke[0], stroke[1] = stroke[1], stroke[0]
print(' '.join(stroke))
