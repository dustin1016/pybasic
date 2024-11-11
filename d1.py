numbers = range(1, 16) ##creates a list of numbers from 1-15


##      TASK
## Loop over the numbers and create the corresponding outputs:
## if a number is divisible by 3, print "Fizz"
## if a number is divisible by 5, print "Buzz"
## if a number is divisible by both 3 and 5, print "FizzBuzz"
for number in numbers:
    if (number%5) == 0 and (number%3) == 0:
        print("fizzbuzz")
    elif (number%5) == 0:
        print("buzz")
    elif (number%3) == 0:
        print("fizz")
    else:
        print(number)