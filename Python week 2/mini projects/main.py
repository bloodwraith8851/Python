# main.py - Entry point for report card system
from student_repot_card import get_subjects, report_card

print("🎓 Student Performance Dashboard")

students_data = []  # Store all student records for future stats

try:
    num_students = int(input("Enter number of students: "))
    if num_students <= 0:
        print("❌ Number must be greater than zero.")
    elif num_students > 50:
        print("❌ Too many students. Max allowed is 50.")
    else:
        for count in range(num_students):
            print("\n===========================================")
            print(f"Entering data for Student {count + 1}")
            print("===========================================")

            name = input("\nEnter student name: ")
            if name.strip() == "":
                print("❌ Name cannot be empty. Skipping student.")
                continue

            subjects = get_subjects()
            students_data.append({"name": name, "subjects": subjects})
            report_card(name, subjects)

except ValueError:
    print("❌ Please enter a valid number of students.")

print("\n🎉 All student data processed successfully!")