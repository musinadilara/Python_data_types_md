
data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]

subjects_grades = {}

for item in data:
    student, subject, grade = item["student"], item["subject"], item["grade"]
    if subject in subjects_grades:
        subjects_grades[subject].update({student: grade})
    else:
        subjects_grades[subject] = {}
        subjects_grades[subject].update({student: grade})

print('Успеваемость учеников по предметам', subjects_grades)
