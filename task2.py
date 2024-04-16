stroke = str(input('Введите строку: ')).lower()  # привожу строку к нижнему регистру
first_letter, last_letter = stroke[:1], stroke[len(stroke)-1:]
stroke = stroke[1: len(stroke)-1]
stroke = stroke.replace('h', 'H')
print(first_letter + stroke + last_letter)
