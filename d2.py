## TASK - CLASS Average grade calculator

## CREATE a dictionary with 5 entries
## the dictionary must have the name of a student as its key and the value is a grade (60-100) example {'Pedro':99}


## After creation, calculate the average grade of the class by looping through the dictionary and print the output based on the values you calculated
## average grade 90 or higher print "The average grade of the class is A"
## average grade in the range of 80 to 89 print "The average grade of the class is B"
## average grade in the range of 70 to 79 print "The average grade of the class is C"
## average grade in the range of 60 to 69 print "The average grade of the class is D"
## average grade is lower than 60 print "The average grade of the class is F"

grades = {
    'a':78,
    'b':88,
    'c':98,
    'd':81,
    'e':75,
}

#Initialize the total grade variable
totalGrade = 0

for grade in grades:
    gr = grades[grade]
    totalGrade += gr


averageGrade = totalGrade/5

print(averageGrade)