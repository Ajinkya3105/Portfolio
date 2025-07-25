# SGPA Calculator
def calculate_sgpa():
    total_points = 0
    total_credits = 0
    subjects = int(input("Enter number of subjects: "))
    
    for i in range(subjects):
        grade = float(input(f"Enter grade point for subject {i+1}: "))
        credit = int(input(f"Enter credit for subject {i+1}: "))
        total_points += grade * credit
        total_credits += credit

    sgpa = total_points / total_credits
    print(f"\nYour SGPA is: {round(sgpa, 2)}")

# CGPA Calculator
def calculate_cgpa():
    semesters = int(input("\nEnter number of semesters: "))
    total_sgpa = 0

    for i in range(semesters):
        sgpa = float(input(f"Enter SGPA for semester {i+1}: "))
        total_sgpa += sgpa

    cgpa = total_sgpa / semesters
    print(f"\nYour CGPA is: {round(cgpa, 2)}")

# Main program
calculate_sgpa()
calculate_cgpa()
