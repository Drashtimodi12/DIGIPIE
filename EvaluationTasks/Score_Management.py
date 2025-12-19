"""
Question 1: Python Basics Objective
Test understanding of Python fundamentals.
Problem Statement: Create a Student Score Management Program.

Requirements=
Ask the user to enter:
Student name
Student score

Store student data in a dictionary

Use:
if / else to check Pass / Fail (Pass ≥ 40)
Loop to handle multiple students
A function to calculate average score
try / except to handle invalid score input 
"""


# --------------------------------
# function calculate average score
# --------------------------------
def average_score(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores) / len(scores) 

# --------------------------------
# Data store in dictionary
# --------------------------------
students = {}

# --------------------------------
# Ask the user to enter name and score
# --------------------------------
while True:
    
    # Student name and score
    print("\n******* WELCOME STUDENTS *******")
    print("1. Store student details. ")
    print("2. Exit")
    
    try: 
        choice = int(input("Enter your choice(1 or 2): "))
    except ValueError as e:
        print("Invalid input! Please enter only 0 or 1.")
        continue

    if choice == 1:
        name = input("\nEnter your name: ").title()
        try:
            score = float(input("Enter your score out of 100: "))
            if score < 0 or score > 100:
                print("Invalid Socore! Enter score between 0 to 100.")
                continue
        except ValueError as e:
            print("Invalid input! Please enter only a number")
            continue

        # Pass or Fail
        if score >= 40:
            result = 'PASS'
        else:
            result = 'FAIL'

        students[name] = {
            "Score" : score
            }
        
        print(f"\n{name} score is {score} ({result}).")

        
    elif choice == 2:
        print("******* THANKY FOR VISIT *******")
        break
    else:
        print("Invalid Choice! Please selecte 1 or 2.")


# --------------------------------
# Calculate average score
# --------------------------------
Scores = []
for data in students.values():
    Scores.append(data["Score"])

avg = average_score(Scores) 

# --------------------------------
# display all result
# --------------------------------
print("\nAll Student Data is:")
for name, data in students.items():
    print(f"{name} (Score: {data['Score']}, {result})")

print("\nAverage score is ", avg)