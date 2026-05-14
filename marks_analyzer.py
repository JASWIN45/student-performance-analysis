import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Student names
students = np.array(["Srushti", "Aman", "Rahul", "Priya", "Karan"])

# Subjects
subjects = np.array(["Maths", "Science", "English"])

# Marks data
marks = np.array([
    [85, 90, 78],
    [45, 50, 60],
    [76, 88, 91],
    [90, 95, 89],
    [35, 40, 30]
])

# Design Header
print(Fore.CYAN + "\n" + "=" * 60)
print("        STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 60 + "\n")

# Student Analysis
for i in range(len(students)):

    print(Fore.YELLOW + f"👨‍🎓 Student: {students[i]}")

    for j in range(len(subjects)):
        print(f"   📘 {subjects[j]} : {marks[i][j]}")

    total = np.sum(marks[i])
    average = np.mean(marks[i])

    print(Fore.BLUE + f"   📊 Total Marks : {total}")
    print(Fore.BLUE + f"   📈 Average     : {round(average, 2)}")

    # Grade Calculation
    if average >= 90:
        grade = "A+"

    elif average >= 75:
        grade = "A"

    elif average >= 60:
        grade = "B"

    elif average >= 40:
        grade = "C"

    else:
        grade = "F"

    print(Fore.MAGENTA + f"   🏅 Grade       : {grade}")

    # Pass/Fail
    if average >= 40:
        print(Fore.GREEN + "   ✅ Status      : PASS")

    else:
        print(Fore.RED + "   ❌ Status      : FAIL")

    print(Fore.CYAN + "-" * 60)

# Overall Analysis
print(Fore.CYAN + "\n" + "=" * 60)
print("               OVERALL CLASS ANALYSIS")
print("=" * 60 + "\n")

# Subject averages
subject_averages = np.mean(marks, axis=0)

for j in range(len(subjects)):
    print(Fore.YELLOW +
          f"📚 {subjects[j]} Average Marks : {round(subject_averages[j], 2)}")

# Student totals
student_totals = np.sum(marks, axis=1)

# Class topper
topper_index = np.argmax(student_totals)

print(Fore.GREEN + f"\n🏆 Class Topper : {students[topper_index]}")
print(Fore.GREEN +
      f"🎯 Topper Total Marks : {student_totals[topper_index]}")

# Subject toppers
print(Fore.CYAN + "\n" + "=" * 60)
print("                 SUBJECT TOPPERS")
print("=" * 60 + "\n")

for j in range(len(subjects)):

    highest_index = np.argmax(marks[:, j])

    print(Fore.MAGENTA +
          f"🥇 {subjects[j]} Topper : "
          f"{students[highest_index]} "
          f"({marks[highest_index][j]} marks)")

# ------------------ GRAPH 1 ------------------

plt.figure(figsize=(8, 5))

plt.bar(students, student_totals)

plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Total Marks")

plt.tight_layout()

# Save graph
plt.savefig("student_total_marks.png")

# Show graph
plt.show()

# ------------------ GRAPH 2 ------------------

plt.figure(figsize=(6, 5))

plt.bar(subjects, subject_averages)

plt.title("Subject Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.tight_layout()

# Save graph
plt.savefig("subject_average_marks.png")

# Show graph
plt.show()

print(Fore.CYAN + "\n📁 Graphs saved successfully!")
print(Fore.CYAN + "   -> student_total_marks.png")
print(Fore.CYAN + "   -> subject_average_marks.png")

print(Fore.GREEN + "\n✅ Project Execution Completed Successfully!\n")

print(Style.RESET_ALL)