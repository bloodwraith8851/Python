# student_report_card.py

# 🎯 Function: Determine Grade from Average
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 85:
        return "A-"
    elif avg >= 80:
        return "B+"
    elif avg >= 75:
        return "B"
    elif avg >= 70:
        return "B-"
    elif avg >= 65:
        return "C+"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"

# 🆕 Function: Grade for Each Subject
def subject_grades(subjects):
    grades = {}
    for subject, mark in subjects.items():
        if mark >= 90:
            grades[subject] = "A"
        elif mark >= 80:
            grades[subject] = "B"
        elif mark >= 70:
            grades[subject] = "C"
        elif mark >= 60:
            grades[subject] = "D"
        else:
            grades[subject] = "F"
    return grades

# 🔍 Function: Check Pass/Fail per Subject
def status_check(subjects):
    return all(mark >= 35 for mark in subjects.values())

# 🆕 Function: Grace Marks Application
def apply_grace_marks(subjects):
    for subject in subjects:
        if 30 <= subjects[subject] < 35:
            subjects[subject] += 5

# 💬 Function: Remarks Based on Grade and Status
def remark(grade, status):
    if grade == "A" and status:
        return "Outstanding performance!"
    elif grade == "A-" and status:
        return "Excellent work!"
    elif grade in ["B+", "B"] and status:
        return "Very Good! Keep improving."
    elif grade == "B-" and status:
        return "Good but needs focus."
    elif grade in ["C+", "C"] and status:
        return "Needs Improvement."
    elif grade == "D" and status:
        return "On Watch. Work harder."
    elif grade == "E" and status:
        return "Barely passed. Caution advised."
    elif not status:
        return "Fail - Needs Re-evaluation"
    else:
        return "Invalid Result"

# 📝 Function: Get Marks from User
def get_subjects():
    subjects = {}
    print("\nEnter marks for 5 subjects (0–100):")
    for subject in ["Math", "Science", "English", "History", "Computer"]:
        while True:
            try:
                mark = int(input(f"{subject}: "))
                if mark < 0 or mark > 100:
                    print("❌ Enter a number between 0 and 100.")
                elif mark >= 0 and mark <= 100:
                    subjects[subject] = mark
                    break
                else:
                    print("❌ Unexpected input.")
            except ValueError:
                print("❌ Invalid input. Enter a number.")
    return subjects

# 🧾 Function: Generate Report Card
def report_card(name, subjects):
    apply_grace_marks(subjects)
    total = sum(subjects.values())
    count = len(subjects)
    average = total / count if count > 0 else 0

    grade = get_grade(average)
    passed = status_check(subjects)
    comment = remark(grade, passed)
    grades = subject_grades(subjects)

    performance = "High" if average > 85 else "Mid" if average > 60 else "Low"
    fail_count = sum(1 for mark in subjects.values() if mark < 35)

    print("\n========== STUDENT REPORT CARD ==========")
    print(f"Name        : {name}")
    for subject, mark in subjects.items():
        print(f"{subject:10}: {mark}   Grade: {grades[subject]}")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Grade       : {grade}")
    print(f"Status      : {'Passed' if passed else 'Failed'}")
    print(f"Remarks     : {comment}")
    print(f"Performance : {performance}")
    print(f"Failures    : {fail_count} Subject(s)")

    if average >= 95 and all(mark >= 90 for mark in subjects.values()):
        print("🏅 Top Performer!")

    if passed:
        if average >= 85:
            print("🏆 Distinction")
        elif average >= 60:
            print("🥈 First Class")
        elif average >= 50:
            print("🥉 Second Class")
        else:
            print("✅ Pass")
    else:
        if average < 40 and any(mark < 30 for mark in subjects.values()):
            print("🚨 Serious Academic Warning")
        else:
            print("⚠️ Needs Improvement in Specific Subjects")

    print("==========================================\n")