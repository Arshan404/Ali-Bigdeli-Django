from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ساختن options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("detach", True)  # مرورگر بعد از اتمام بسته نشه
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# مسیر کروم‌درایور
service = Service("D:/chromedriver/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://google.com")

# پیدا کردن نوار سرچ
search_bar = driver.find_element("name", "q")
search_bar.send_keys("آموزش پایتون مکتبخونه")
search_bar.send_keys(Keys.ENTER)

# گرفتن کد HTML صفحه
soup = BeautifulSoup(driver.page_source, "html.parser")
name_list = soup.find_all('h3')

# ذخیره کردن در فایل
with open("names.txt", "a", encoding="utf-8") as f:
    for name in name_list:
        f.write(name.text.strip())
        f.write("\n")


"""
پروژه کنترل عملکرد مرورگر و دریافت اطاعات صفحات
در این پروژه قصد داریم با یکی از ماژول های کاربردی برای کنترل مرورگر کار کنیم که به برنامه نویس توانایی کنترل عملکرد های متفاوتی از جمله باز کردن صفحات کلیک و یا نوشتن را توسط برنامه نویسی میدهد.

 

قبل شروع نیاز است تا عملکرد کلی را با هم مرور کنیم:

1. باز کردن صفحات وب از جمله گوگل با ماژول مربوطه

2. جست و جوی کلید واژه های مد نظر در وب

3. استخراج لیستی از آیتم های مورد نیاز و ذخیره سازی در فایل

 

ماژول selenium یک پکیج بسیار کاربردی در موارد مختلف است که از تست و جمع آوری اطلاعات وب گرفته و تا تست مسائل امنیتی کاربردی است.

 

پس از نصب ماژول مربوطه کافیست که برای ارتباط با آن درایور مرتبط با مرورگر خود را از طریق لینک زیر دانلود نمایید.(شاید نیاز به تغییر آیپی باشد) باید اشاره شود که در این پروژه مد نظر مرورگر Chrome است و از درایور مبتنی بر آن استفاده خواهیم کرد. درایوری که انتخاب می شود می بایست با نسخه مرورگر نصب شده در سیستم شما مطابقت داشته باشد.

 

https://chromedriver.chromium.org/downloads

 

بر اساس سیستم عاملی که دارید نسخه مربوطه را بارگیری نمایید.

سپس فایل مروبطه را به پوشه پروژه منتقل نمایید.

 

باز کردن صفحات وب از جمله گوگل با ماژول مربوطه
حال برای ساخت آبجکت درایور و کد پایتون می توانید به شکل زیر عمل کنید. به بزرگ و کوچک بودن حروف دقت نمایید.

 

برای اینکه ماژول بتواند درایور مربوطه را پیدا کند می بایست در آپشن های ورودی آرگومان executable_path  را برابر آدرس فایل مربوطه قرار دهید.

 

from selenium.webdriver import Chrome
driver = Chrome (executable_path=”chromedriver.exe”)

 

در ادامه برای باز کردن صفحه مد نظر می توانید با اعمال متد get بر روی driver به مقصود خود که باز کردن یک آدرس وب است دست پیدا کنید.

 

driver.get(“https://google.com”)
 

جست و جوی کلید واژه های مد نظر در وب
در این قسمت می خواهیم در صفحه مربوطه به دنبال یک المان مخصوص که دارای یک attribute با نام q است بگردیم که برای این کار می توانیم از متد find_element_by_name استفاده نماییم.

 

search_bar = driver.find_element_by_name(“q”)
 

پس از دریافت و ذخیره سازی آن در کی متغیر حال می توانیم با استفاده از متد send_keys به المان موجود در صفحه رشته هایی از کارکتر برای تایپ ارسال نماییم.

 

search_bar.send_keys(“anything”)
 

سپس برای اینکه بتوانید بر روی المان ایجاد شده کلید Enter را اعمال کنیم به روش زیر عمل می کنیم:

 

from selenium.webdriver.common.keys import Keys
search_bar.send_keys(Key.ENTER)

 

استخراج لیستی از آیتم های مورد نیاز و دخیره سازی در فایل
اما در این بخش نیاز است که اطلاعت صفحات را استخراج و از درون آن اطلاعات خاصی را با تگ های مربوطه بدست آورد. که در این میان از ماژولی با نام bs4   یا BeautifulSoup استفاده می کنیم. این ماژول به توسعه دهنده این اجازه را می دهد تا بتواند در سورس کد صفحات به دنبال اطلاعات مورد نیاز خود گشته و آن ها را بازیابی نماید.

 

برای دریافت اطلاعت و سورس یک صفحه می توانید از روش زیر استفاده نمایید.

 

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source)

 

حال می بایست در آبجکت ایجاد شده به دنبال تگ های h3 گشته و اطلاعات تیتر لینک ها را باز یابی نماییم.

 

name_list = soup.find_all(‘h3’)
 

و در نهایت با ایجاد یک پیمایش بر روی المان های لیست می توان آنها را به ترتیب درون یک فایل ذخیره کرد.

 

with open(‘names.txt’,’a’,encoding(‘utf-8’)) as f:
    for name in name_list:
         f.write(name)
 

و اما در موجوع پس از ادغام تمام عملکرد ها به کد زیر خواهیم رسید:

 



# importing needed library
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# creating driver object
driver = Chrome(executable_path='chromedriver.exe')

# calling a web page by url
driver.get("https://google.com")

# finding search bar element by name 
search_bar = driver.find_element_by_name('q')

# sending and typing inside the element
search_bar.send_keys("آموزش پایتون مکتبخونه")

# using Keys class to hit enter
search_bar.send_keys(Keys.ENTER)

# creating a soup object
soup = BeautifulSoup(driver.page_source)

# fetching all h3 tags from source page
name_list = soup.find_all('h3')

# creating a file and writing all the names in name_list inside it
with open('names.txt','a',encoding='utf-8') as f:
    for name in name_list:
        f.write(name)
"""

