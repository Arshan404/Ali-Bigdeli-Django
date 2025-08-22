import random

def odd_or_even(number):
    if number % 2 == 0 :
        return "even"
    else:
        return "odd"
    
random_number = random.randint(1,100)

print("Random number : " , random_number)
print(odd_or_even(random_number))