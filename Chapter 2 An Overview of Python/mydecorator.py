import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()   # مقدار تابع اصلی رو ذخیره کن
        elapsed = time.time() - start
        print('took {} seconds to execute'.format(elapsed))
        return result     # مقدار رو برگردون
    return wrapper

@timer
def counter():
    total = 0
    for i in range(0 , 100000):
        total += 1
    return total

print(counter())

"""
decorator در پایتون
پایتون از ویژگی جالبی به نام دکوراتورها برای افزودن قابلیت به کد موجود برخوردار است.

 

به این برنامه metaprogramming نیز گفته می شود زیرا بخشی از برنامه سعی می کند قسمت دیگری از برنامه دیگری را در زمان اجرا در بر گیرد و اصلاحاتی را صورت دهد.

 

توابع در پایتون شهروندان درجه یک هستند که بدان معناست که از عملیاتی مانند آرگومان ، برگشت از یک تابع ، اصلاح و اختصاص به یک متغیر پشتیبانی می کنند که در واقع مفهومی اساسی است که باید قبل از شروع ایجاد دکوراتور های پایتون درک کنید.

 

اختصاص توابع به متغیرها
برای شروع کار ما تابعی ایجاد می کنیم که هر زمان فراخوانی شود یک عدد به آن اضافه می شود. سپس ما تابع را به یک متغیر اختصاص می دهیم و از این متغیر برای فراخوانی تابع استفاده می کنیم.

def plus_one(number):
    return number + 1
add_one = plus_one
add_one(5)

 

تعریف توابع در داخل سایر توابع
در مرحله بعدی ، ما نشان خواهیم داد که چگونه می توانید یک تابع را در داخل یک تابع دیگر در پایتون تعریف کنید.به زودی خواهیم فهمید که همه اینها در ایجاد و درک دکوراسیون در پایتون چگونه مرتبط است.

def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result
plus_one(4)
 
 

عبور توابع به عنوان آرگومان به سایر توابع
توابع همچنین می توانند به عنوان پارامتر به سایر توابع منتقل شوند. بیایید این را در زیر نشان دهیم.

 

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
 

توابع  برای بازگردانی توابع دیگر
یک تابع همچنین می تواند عملکرد دیگری تولید کند. در زیر با استفاده از یک مثال آن را نشان خواهیم داد.

 

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()
 

توابع Nested به محدوده متغیر Enclosing Function دسترسی دارند.

پایتون به یک تابع تو در تو اجازه می دهد تا به محدودیت عملکرد خارجی محرمانه دسترسی پیدا کند. این یک مفهوم حیاتی در دکوراتورها است - این الگو به عنوان بسته شدن باعث می شود.

def print_message(message):

    "Enclosing Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()
print_message("Some random message")
 
 

ایجاد دکوراتورها
با استفاده از این پیش نیازها بیایید جلو برویم و یک دکوراتور ساده بسازیم که یک جمله را به بزرگ تبدیل کند. ما این کار را با تعریف یک بسته بندی داخل یک تابع محصور انجام می دهیم. همانطور که مشاهده می کنید بسیار شبیه به عملکرد موجود در یک تابع دیگر است که قبلاً ایجاد کردیم.

 

def uppercase_decorator(function):

    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
 
 

تابع دکوراتور ما یک تابع را به عنوان آرگومان می گیرد ، بنابراین ما باید یک تابع را تعریف کرده و به دکوراتور خود منتقل کنیم. قبلاً یاد گرفتیم که می توانیم یک تابع را به یک متغیر اختصاص دهیم. ما برای فراخوانی عملکرد دکوراتور خود از این ترفند استفاده خواهیم کرد.

 

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)

decorate()
 
 

با این حال ، پایتون روش بسیار ساده تری را برای استفاده از دکوراتور در اختیار ما قرار می دهد. ما به سادگی از نماد @ قبل از عملکردی که می خواهیم دکور کنیم استفاده می کنیم. اجازه دهید در عمل نشان دهیم که در زیر به خوبی نشان داده شده است.

@uppercase_decorator

def say_hi():
    return 'hello there'

say_hi()
 
"""
