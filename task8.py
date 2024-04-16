list_of_first, list_of_second = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
result_first = list_of_first + list_of_second  #конкатенация
list_of_second.insert(0, list_of_first[0])  #применение метода insert
list_of_second.insert(1, list_of_first[1])
list_of_second.insert(2, list_of_first[2])
list_of_second.insert(3, list_of_first[3])
list_of_second.insert(4, list_of_first[4])
result_second = list_of_second
print('\n', result_first, '\n',  result_second)

