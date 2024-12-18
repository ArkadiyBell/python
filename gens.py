def fibonachi_gen(n):
    a=0
    b=1
    
    c=0
    while c < n:
        yield a
        a+=b
        c+=1
        if c+1<=n:
            yield b 
            b+=a
            c+=1
   
print('8 первых 8 чисел Фибоначчи: ')
print([_ for _ in fibonachi_gen(8)])

###############################################################################
import math
def is_prime(n):
    if n < 2 or not type(n) is int:
        return False
    d=2
    while d <= math.sqrt(n):
        if (n / d) % 1 == 0:
            return False
        d+=1
    return True


def prime_mn_gen(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            yield i
    

print('Простые делители числа 2*3*5*19*101:')
print([_ for _ in prime_mn_gen(2*3*5*19*101)])

###############################################################################

def degree_gen(n, degree):
    for i in range(1, degree):
        yield n**i

a = 3
print('Возведение числа 3 в степени от 1 до 15')
print([_ for _ in degree_gen(a, 15)])

###############################################################################

def primes_in_range_gen(start, stop):
    for i in range(start+1, stop):
        if is_prime(i):
            yield i
print('Простые числа в диапазоне (-100, 900)')
print([_ for _ in primes_in_range_gen(-100, 900)])
    
    
    
    
