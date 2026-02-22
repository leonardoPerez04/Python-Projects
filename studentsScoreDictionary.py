student_scores = {
    'Harry':88,
    'Ron':78,
    'Hermione':95,
    'Draco':75,
    'Neville':60
}
student_grades={}
for key in student_scores:
    if student_scores[key]>=91 or student_scores[key]<=100:
        student_grades[key]="Outstanding"
    elif student_scores[key]>=81 or student_scores[key]<=90:
        student_grades[key]="Outstanding"
    elif student_scores[key]>=71 or student_scores[key]<=80:
        student_grades[key]="Outstanding"
    else:
        student_grades[key]="Outstanding"
for key in student_grades:
    print(key)
    print(student_grades[key])
for key in student_scores:
    print(key)
    print(student_scores[key])