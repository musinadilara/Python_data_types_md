
students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

marks = {student["name"]: sum(student["grades"]) / len(student["grades"]) for student in students}
print('Успеваемость студентов:', marks,  '.')
print("Студент с наивысшей средней оценкой:", max(marks, key = marks.get) + '.')

