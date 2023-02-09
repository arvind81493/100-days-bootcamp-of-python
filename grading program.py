students_scores={
    "harry":85,
    "ron":65,
    "hermaine":95

}
students_grades={}
for students in students_scores:
    score=students_scores[students]
    if score >90:
        students_grades[students]="outstanding"
    elif score >80:
        students_grades[students]="Exceeds Expectation"
    elif score>70:
        students_grades[students]="acceptable"
    else:
        students_grades[students]="FAIL"
print(students_grades)
        

