a = input("Введите строку ")
print(a[2], a[-2], a[0:5], a[:-2], a[0::2], a[1::2], a[::-1], a[-1::-2], a[-2:0:-1], len(a), sep='\n')
a = input("Введите строку ")
if len(a) % 2 == 0:
    b = a[:int(len(a)/2)]
    print(a[int(len(a)/2):]+b)
else:
    b = a[:int(len(a)/2+1)]
    print(a[int(len(a)/2+1):]+b)
x = 0
while x <= 10:
    print(x, end=' ')
    x += 1
x = 20
while x >= 1:
    print(x, end=' ')
    x -= 1

x = int(input())
i = 0
while x % 2 == 0:
    x = x / 2
    i += 1
print(i)

l = [1, 2, 3, 4, 5, 6, 7, 8]
while range(len(l)):
    l.pop(0)
    print(l)

l = [2, 1, 4, 6, 5, 8, 7]
while range(len(l)):
    l.sort()
    l.pop(0)
    print(l)

a = input("Введите число: ")
b = input("Введите число: ")
try:
    a = float(a)
    b = float(b)
    s = a + b
except ValueError:
    s = a + b
finally:
    print(s)


print("Введите стороны треугольника")
a = int(input())
b = int(input())
c = int(input())
def tri(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
print(tri(a, b, c))

print("Введите год")
a = int(input())
def year(a):
    if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
        return False
    else:
        return True
print(year(a))



