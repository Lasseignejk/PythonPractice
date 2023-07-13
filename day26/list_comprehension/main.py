numbers = [1,2,3]
new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

name = "Jaye"
new_name = [letter for letter in name]
# print(new_name)


range_list = [num*2 for num in range(1,5)]
# print(range_list)

conditional_list = [num for num in range(1,11) if num % 2 == 0]
# print(conditional_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

uppercase_names = [name.upper() for name in names if len(name) > 4]
# print(uppercase_names)

import random

students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    # print(row)
    # print(row.student)
    # print(row.score)