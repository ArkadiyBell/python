from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        if ("a"<=horizontal<="h"):
            self.horizontal=horizontal
        else: raise ValueError("Неверное значание горизонтали")
        if (1<=vertical<=8):
            self.vertical=vertical
        else: raise ValueError("Неверное значание веритикали")
    @abstractmethod
    def can_move(self):
        pass
    
class King(ChessPiece):
    def can_move(self, h, v):
        if ("a"<=h<="h" and 1<=v<=8):
            if (abs(ord(self.horizontal)-ord(h))<=1 and abs(self.vertical-v)<=1 and
                abs(ord(self.horizontal)-ord(h))+abs(self.vertical-v)!=0):
                return True
            else: return False
        else: raise ValueError("Неверная координата")

class Knight(ChessPiece):
    def can_move(self, h, v):
        if ("a"<=h<="h" and 1<=v<=8):
            if ((abs(ord(self.horizontal)-ord(h))==2 and abs(self.vertical-v)==1) or
                (abs(ord(self.horizontal)-ord(h))==1 and abs(self.vertical-v)==2)):
                return True
            else: return False
        else: raise ValueError("Неверная координата")
        

king = King('d', 4)
knight = Knight('b', 7)
print(f"Король может сходить так, если его координаты: {king.horizontal}{king.vertical}")
print(" abcdefgh")
chessDeskKing="".join([str(v+1)+"".join(["+" if king.can_move(chr(ord("a")+h), v+1) else "-"
                                         for h in range(8) ])+"\n"for v in range(8)])
print(chessDeskKing)

print(f"Конь может сходить так, если его координаты: {knight.horizontal}{knight.vertical}")
print(" abcdefgh")
chessDeskKnight="".join([str(v+1)+"".join(["+" if knight.can_move(chr(ord("a")+h), v+1) else "-"
                                           for h in range(8) ])+"\n"for v in range(8)])
print(chessDeskKnight)
#############################################################################################################
class Father:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = "strict"


class Mother:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = "kind"


class Daughter(Mother, Father):
    def __init__(self, mood="neutral"):
        super().__init__(mood)


class Son(Father, Mother):
    def __init__(self, mood="neutral"):
        super().__init__(mood)

#############################################################################################################

class USADate:
    def __init__(self, year, month, day):
        if month>9:
            m=str(month)
        else: m="0"+str(month)
        
        if day>9:
            d=str(day)
        else: d="0"+str(day)
        
        y=str(year)
        y=(4-len(y))*"0"+y
        
        self.d=d
        self.m=m
        self.y=y
    def format(self):
        return self.m + '-' + self.d + '-' + self.y
    def iso_format(self):
        return self.y + '-' + self.m + '-' + self.d
    
class ItalianDate(USADate):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)
    def format(self):
        return self.d + '-' + self.m + '-' + self.y
        
        
print("США: "+ USADate(157, 10, 6).format())
print("Италия: "+ItalianDate(2024, 11, 23).format())
print(USADate(2006, 7, 11).iso_format())
print(ItalianDate(1994, 5, 7).iso_format())












