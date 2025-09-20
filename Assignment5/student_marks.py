
student_marks = {
    "Aman": 85,
    "Riya": 92,
    "Kabir": 78,
    "Simran": 88,
    "Arjun": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
