from functools import singledispatchmethod

class Navigator:
    def __init__(self):
        pass
    @singledispatchmethod
    def neg(self, param):
        raise TypeError("Аргумент переданного типа не поддерживается")
        
    @neg.register(int)
    def int_neg(self, param):
        return -param
    
    @neg.register(float)
    def float_neg(self, param):
        return -param
    
    @neg.register(bool)
    def bool_neg(self, param):
        return not (param)

nav = Navigator()


print('int 2: ' + str(nav.neg(2)))
print('float 2.5: ' + str(nav.neg(2.5)))
print('bool False: ' + str(nav.neg(True)) + "\n")


############################################################################
import datetime
class date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
    def __str__(self):
        if self.month>9:
            m=str(self.month)
        else: m="0"+str(self.month)
        
        if self.day>9:
            d=str(self.day)
        else: d="0"+str(self.day)
        
        y=str(self.year)
        y=(4-len(y))*"0"+y
        return y+"-"+m+"-"+d

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")
    @__init__.register(date)
    def date__init__(self, birth_date):
        self.birth_date=birth_date
    @__init__.register(str)
    def iso__init__(self, birth_date):
        self.birth_date=date(*(map(int, birth_date.split("-"))))
    @__init__.register(list)
    def list__init__(self, birth_date):
        self.birth_date=date(*birth_date)
    @__init__.register(tuple)
    def set__init__(self, birth_date):
        self.birth_date=date(*birth_date)
        
    def age(self):
        result = 0
        dt = datetime.datetime.now()
        to_day = date(dt.year, dt.month, dt.day)
        result+= to_day.year - self.birth_date.year - 1
        if to_day.month > self.birth_date.month or (to_day.day >= self.birth_date.day and to_day.month == self.birth_date.month):
            result+=1
        return result
        




date1=BirthInfo(date(2023, 2, 26))
print(f'С {date1.birth_date} прошло лет: {date1.age()}')
date2=BirthInfo([2022, 12, 21])
print(f'С {date2.birth_date} прошло лет: {date2.age()}')

        
        
        
        
        
        
        
        
        
        
        
        
        
        