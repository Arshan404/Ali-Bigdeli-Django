"""
2- تابعی بنویسید که در آن ورودی عددی از کاربر گرفته و سپس دنباله عددی را از 0 تا عدد ورودی کاربر ایجاد کند. سپس اعداد بدست آمده را جمع کرده و جواب نهایی را بازگرداند.

"""

def squence_sum_interactive():
    n = int(input("Enter a non-negative integer : "))
    if n < 0 :
        raise ValueError("n must be non-negative")
    seq = list(range(0 , n + 1))
    print("sequence : " , seq)
    return sum(seq)

result = squence_sum_interactive()
print(result)
