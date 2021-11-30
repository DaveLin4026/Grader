#! /usr/bin/python3

### Grader by David Linares ###
### Testing conditional statemnts ### 

# Pass the grade score as an integer
grade = int(input("Please enter your grade score: "))
# Print confirmation of passing grade
if grade >= 65:
    print("Passing grade of:")

# Scoring metric for 90+ grades
    if grade >= 90:
        if grade > 96:
            print("A+")

        elif grade > 93 and grade <= 96:
            print("A")

        elif grade >= 90:
            print("A-")

    # Scoring metric for 80+ grades
    elif grade >=80:
        if grade > 86:
            print("B+")

        elif grade > 83 and grade <= 86:
            print("B")

        elif grade >= 80:
            print("B-")

    # Scoring metric for 70+ grades
    elif grade >=70:
        if grade > 76:
            print("C+")

        elif grade > 73 and grade <= 76:
            print("C")

        elif grade >= 70:
            print("C-")

    elif grade >= 65:
        print("D")
# Grades below 65 are failing
else:
    print("Failing grade")
