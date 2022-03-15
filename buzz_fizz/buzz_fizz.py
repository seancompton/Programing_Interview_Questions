multiples = [3, 5, 6]
INCRAMENTS = 100

def is_buzz_or_fizz(number, multiples):
    fizz_or_buzz = ""
    x = 0
    words = ["buzz", "fizz", "bizz", "dizz", "wizz", "vizz"]

    for i in range(len(multiples)):
        if(number % multiples[i] == 0):
            fizz_or_buzz = fizz_or_buzz + words[i]
    
    if fizz_or_buzz == "":
        return number

    else: 
        return fizz_or_buzz      

for i in range(1, INCRAMENTS):
    print(is_buzz_or_fizz(i, multiples))