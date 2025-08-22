def count_chars_and_numbers(text):
    letters = 0
    numbers = 0
    for char in text:
        if char.isalpha():
            letters +=1
        elif char.isdigit():
            numbers +=1
    return{"characters" : letters , "numbers" : numbers}

user_input = input("Enter your text : ")
result  = count_chars_and_numbers(user_input)
print(result)