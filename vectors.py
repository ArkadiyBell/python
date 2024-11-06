import math
class Vector2d:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

        self.x=x2-x1
        self.y=y2-y1
    #длина вектора
    def length(self):
        x=self.x
        y=self.y
        return math.sqrt((x)**2+(y)**2)
    #Угол между вектором и осью х
    def angle(self):
        x=self.x
        y=self.y
        an=math.degrees(math.atan(abs(x)/abs(y)))
        return an if x>=0 else an+90
    #Возвращает проекцию результирующего вектора суммы двух векторов
    def summ(self, vec):
        x=self.x
        y=self.y
        res=Vector2d(0,0 ,x+vec.x,y+vec.y)
        return [res.x, res.y]
    #Возвращает проекцию результирующего вектора разность двух векторов
    def diff(self, vec):
        x=self.x
        y=self.y
        res=Vector2d(0,0 ,x-vec.x,y-vec.y)
        return [res.x, res.y]
    #Скалярное произведение
    def multiply(self,vec):
        x=self.x
        y=self.y
        return x*vec.x+y*vec.y


vector1=Vector2d(*list(map(int, input("Введите через пробел координаты начала и конца первого вектора").split())))
vector2=Vector2d(*list(map(int, input("Введите через пробел координаты начала и конца второго вектора").split())))
print(vector1.length(),vector1.angle(), vector1.summ(vector2),vector1.diff(vector2), vector1.multiply(vector2))
