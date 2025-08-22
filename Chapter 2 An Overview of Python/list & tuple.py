L1 = ["Ali", "Bigdeli",27,['hello',1,2,3]]    
L2 = [1, 2, 3, 4, 5, 6]   
print(type(L1))
print(L1[0])
L1[0] = 'shoji'
print(L1[0])
print(L1[-1])
print(L1[-1][0])
L1.append('shoji')           #اضافه کردن به انتهای لیست
print(L1)
L1.insert(1 , 'sozaneh')     #اضافه کردن با نشان دادن ایندکس  و بقیه آیتم ها هم شیفت میخورن میرن جلو
print(L1)
print(len(L1))
print('hello' in L1)
print(any('hello' in item for item in L1 if isinstance(item, list))) 
print(L1[0:3])                #اسلایس کردن لیست

tuple_t = tuple(L1)           #امکان تغییر دادن در تاپل نیست
print(tuple_t)
print(type((27)))
print(type((27,)))            #اگه بخوایی به یک شاخص تاپل بهش نگاه کنی بعد اینکه تو یک پرانتز دیگه هم گذاشتیش باید جلوش یک کاما بذاری حتی اگه تک عنصری هست تا تاپل بهش نگاه کنه


