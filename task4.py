stroke = str(input('Введите строку: '))
list_of = list(stroke)
count_of_words = int(list_of.count(' ')) + 1
print(f"В вашей строке было {count_of_words} слов(-а)")
