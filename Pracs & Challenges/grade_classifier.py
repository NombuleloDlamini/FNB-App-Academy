"""Practical Task
Task Overview 

Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects,
calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must 
correctly use conditionals for all grade and status logic.

Requirements 

Collect learner name and marks for three subjects (as floats) using input()
Calculate the average mark across the three subjects
Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
Assign Pass status if the average is 50 or above, Fail otherwise
Flag any individual subject mark below 40 as ‘needs intervention’
Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags


"""

name_and_surname = input("Enter your name and surname: ").title()
subject1_mark = float(input("Enter your first subject mark: "))
subject2_mark = float(input("Enter your second subject mark: "))
subject3_mark = float(input("Enter your third subject mark: "))

average_mark = float((subject1_mark+subject2_mark+subject3_mark)/3)

if average_mark > 100 or average_mark < 0:
    print("invalid marks")
    exit


else:
    average_mark = round(average_mark , 2)
    status = " "
    flag = " "
    if average_mark >= 80:
        grade = "A"
    elif average_mark >= 70:
        grade = "B"
    elif average_mark >= 60:
        grade = "C"
    elif average_mark >= 50:
        grade = "D"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

if average_mark >= 50:
    status = "Pass"
else:
    status = "Fail"

if average_mark < 40:
    flag = "Needs Intervention!!"


print(f"Report card for {name_and_surname}:\n subject1_mark: {subject1_mark}\n subject2_mark: {subject2_mark}\n subject3_mark: {subject3_mark}\n Average mark: {average_mark}\n Grade: {grade}\n Status: {status}\n {flag} ")