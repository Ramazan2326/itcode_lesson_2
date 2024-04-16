list_of = str(input('Введите последовательно через пробел'
                    ' фамилию, имя, отчество: ')).split()
surname, name, last_name = list_of[0], list_of[1], list_of[2]
result = surname + ' ' + name[0].upper() + '. ' + last_name[0].upper() + '.'
print(result)
