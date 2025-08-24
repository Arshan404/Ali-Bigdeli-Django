class Human:
    def __init__(self , name , lname):
        self.name = name
        self.lname = lname
    def fullname(self):
        return  self.name + ' '+self.lname
p1 = Human('ali' , 'bigdeli')
#p2 = Human('nazanin')

#p1.name = 'ali'
#p1.lname  = 'bigdeli'

#p2.name = 'hassan'
#p2.lname = 'jabari'

print(p1.fullname())        #چون داخل کلاس تعریف شده پس برای هردو داره ایجاد میشه
##print(p2.manager)
#print(p2.name) 