''' Another option for names, with no limit but making confidence in the input of users is: '''
# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")

names =  []
assignments =  []
grades =  []

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for index in range(2): # Fixed amount to be modified before running the script. The other option is more flexible but needs robustness.
    names.append(str(input("Enter your name: ")))
    assignments.append(int(input("Enter your remaining assignments: ")))
    grades.append(int(input("Enter your grade: ")))

    print(names)
    print(assignments)
    print(grades)

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    #print(message.format(name,assignment,grade))
    increase = grade + 2*assignment
    print(f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to \
submit before you can graduate. Your current grade is {grade} and can increase \
to {increase} if you submit all assignments before the due date.\n\n")