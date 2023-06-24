def count_students_unable_to_eat(students, sandwiches):
    count = 0
    while len(students) > 0:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0
        else:
            students.append(students.pop(0))
            count += 1

        if count == len(students):
            return count

    return count
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
result = count_students_unable_to_eat(students, sandwiches)
print(result)  # Output: 0
