"""Print numbers 1 to 50. For multiples of 3 print 'Fizz', multiples of 5 print 'Buzz', both print 'FizzBuzz'."""

for x in range(1,51):
    if x%3 == 0 and x%5 == 0:
        print("fizzbuzz")
    elif x%3 == 0:
        print("fizz")
    elif x%5 == 0:
        print("buzz")
    else:
        print(x)