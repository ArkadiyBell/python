x = 997
def rk(str):
    result = 0
    for i, val in enumerate(str):
        result+= ord(val)*x**i
    return result 

def search(t, p):
    
    ind=[]
    n=len(t)
    m=len(p)
    deg = x**(m-1)
    p_hash = rk(p)
    sub_hash = rk(t[n-m:n])
    if sub_hash == p_hash:
        ind.append(n-m)
    for i in range( n-m):
        print(n-m-i)
        sub_hash = (sub_hash-deg*ord(t[n-i-1]))*x+ord(t[n-m-i-1])
        if sub_hash == p_hash:
            ind.append(n-m-i-1)
    return ind
    

print(search("asdwawdwawdawda", "w"))


#################################################################


  


class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color 
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.color == other.color
            
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.color != other.color
            
    
    def __hash__(self):
        
        return hash((self.x, self.y, self.color))
        

cp = ColoredPoint(2, 2, "R")
cp1 = ColoredPoint(2, 2, "R")
print(cp==cp1)
points={0:cp1,
        1:ColoredPoint(2, 5, "B"),
        2:ColoredPoint(7, 8, "G"),
        3:ColoredPoint(1, 4, "W"),
        4:ColoredPoint(8, 8, "Y"),
        5:cp
        
        }
print(*[hash(points[_])  for _ in range(6)])    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        