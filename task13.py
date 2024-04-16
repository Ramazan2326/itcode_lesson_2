students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print(f"Способ 1. Все люди: {students | employees}")
print(f"Способ 2. Все люди: {students.union(employees)}")
print(f"Способ 1. Все люди, кто одновременно учится и работает: "
      f"{students & employees}")
print(f"Способ 2. Все люди, кто одновременно учится и работает: "
      f"{students.intersection(employees)}")
print(f"Способ 1. Все люди, кто только работает, но не учится: "
      f"{employees - students}")
print(f"Способ 2. Все люди, кто только работает, но не учится: "
      f"{employees.difference(students)}")
print(f"Способ 1. Все люди, кто либо только учится, либо только работает: "
      f"{(employees - students) | (students - employees)}")
print(f"Способ 2. Все люди, кто либо только учится, либо только работает: "
      f"{(employees.difference(students)).union(students.difference(employees))}")
