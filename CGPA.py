# CGPA Calculator
semesters = int(input("Enter number of semesters: "))
total_sgpa = 0

for i in range(semesters):
    sgpa = float(input(f"Enter SGPA for semester {i+1}: "))
    total_sgpa += sgpa

cgpa = total_sgpa / semesters
print(f"\nYour CGPA is: {round(cgpa, 2)}")
