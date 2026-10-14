students = [
    {
        "name": "Arun",
        "cgpa": 8.2,
        "arrears": 0,
        "python": True
    },
    {
        "name": "Priya",
        "cgpa": 7.2,
        "arrears": 0,
        "python": True
    },
    {
        "name": "Karthik",
        "cgpa": 8.7,
        "arrears": 1,
        "python": True
    }
]


def check_eligibility(student):
    if (student["cgpa"] >= 7.5
            and student["arrears"] == 0
            and student["python"] == True):
        return True
    else:
        return False


for student in students:
    if check_eligibility(student):
        print(student["name"], "→ Eligible")
    else:
        print(student["name"], "→ Not eligible")