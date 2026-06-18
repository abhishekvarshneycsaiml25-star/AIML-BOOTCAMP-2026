students = [
    {
        "name": "Kinjalk Mishra",
        "college_name": "GLA UNIVERSITY",
        "section": "CA",
        "grades": "A+",
        "city": "Lucknow",
        "marks": 95,
        "attendance": 92,
        "lab": True
    },
    {
        "name": "Jai",
        "college_name": "GLA UNIVERSITY",
        "section": "CE",
        "grades": "B",
        "city": "Kanpur",
        "marks": 78,
        "attendance": 85,
        "lab": True
    },
    {
        "name": "Harshit",
        "college_name": "GLA UNIVERSITY",
        "section": "CA",
        "grades": "F",
        "city": "Jaipur",
        "marks": 32,
        "attendance": 48,
        "lab": False
    },
    {
        "name": "Rohan",
        "college_name": "GLA UNIVERSITY",
        "section": "ME",
        "grades": "A",
        "city": "Agra",
        "marks": 88,
        "attendance": 79,
        "lab": True
    },
    {
        "name": "Priya",
        "college_name": "GLA UNIVERSITY",
        "section": "CS",
        "grades": "A+",
        "city": "Delhi",
        "marks": 97,
        "attendance": 96,
        "lab": True
    }
]


def attendance_check(students):
    print("\n===== ATTENDANCE REPORT =====")
    for student in students:
        if student["attendance"] <= 75:
            print(f"{student['name']} has low attendance.")
        else:
            print(f"{student['name']} has high attendance.")


def lab_check(students):
    print("\n===== LAB REPORT =====")
    for student in students:
        if student["lab"]:
            print(f"{student['name']} has taken lab.")
        else:
            print(f"{student['name']} has not taken lab.")


def result_check(students):
    print("\n===== RESULT REPORT =====")
    for student in students:
        if 40 <= student["marks"] <= 79:
            print(f"{student['name']} is Pass.")
        elif 80 <= student["marks"] <= 100:
            print(f"{student['name']} is Distinction.")
        else:
            print(f"{student['name']} is Fail.")


# Main Program
attendance_check(students)
lab_check(students)
result_check(students)