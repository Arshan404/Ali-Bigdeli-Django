class Human:
    def __init__(self , name , lname):
        self.name = name
        self.lname = lname
    def fullname(self):
        return  self.name + ' '+self.lname
    def __str__(self):
        return self.name + ' object'

class Emploee(Human):
    manager = 'Hassan'
    def programmer(self):
        print('yay I am a programmer') 
    def full(self):
        return super().fullname()
p1 = Emploee('ali' , 'bigdeli')
print(p1)
print(p1.manager)
print(p1.programmer())
p1.programmer()
print(p1.full())

"""
وراثت پایتون
وراثت جنبه مهمی از الگوی شی گرا است. وراثت قابلیت استفاده مجدد کد را برای برنامه فراهم می کند زیرا ما می توانیم از کلاس موجود برای ایجاد یک کلاس جدید به جای ایجاد از ابتدا استفاده کنیم.

 

در وراثت ، کلاس کودک ویژگی هایی را به دست می آورد و می تواند به تمام اعضای داده و عملکردهای تعریف شده در کلاس والد دسترسی داشته باشد. کلاس کودک همچنین می تواند پیاده سازی ویژه خود را برای عملکردهای کلاس والدین فراهم کند.

 

در پایتون برای نمایش یک کلاس ارث برده شده در کلاس فرزند می بایست پس از تعریف نام کلاس فرزند در داخل پرانتز نام کلاس والد و یا کلاس های والد آن آورده شود.

 

به نحوه نمایش زیر دقت نمایید:

 

class derive-class(<base class 1>, <base class 2>, ..... <base class n>):  
    <class - suite>   
 

که در واقع عملیات فوقانی نقش انتقال خصوصیت و عملکرد ها را به کلاس فرزند دارد.

 

حال آنکه این خصوصیات و عملکرد ها می توانند در کلاس های متعددی بوده و به کلاس های جدیدی که خصوصیات مشابهی نیاز دارند اعمال شوند.
"""