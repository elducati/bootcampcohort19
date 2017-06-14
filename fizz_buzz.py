def fizz_buzz(num):
    #checks if number is divisible by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    #checks if number if number is divisible by 5    
    elif num % 5 == 0:
        return 'Buzz'
    #checks if number is divisible by 3
    elif num % 3 == 0:
        return 'Fizz'
    #returns number if not divisible by either 3 or 5
    else:
        return num
