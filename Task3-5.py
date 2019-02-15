print("Введите год")
a=int(input())
if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
    print('NO')
else:
    print('YES')

print("Введите стороны треугольника")
a = int(input())
b = int(input())
c = int(input())
if a < b+c and b < a+c and c < a+b:
    print("Yes")
else:
    print("No")

print("Введите три числа")
a = int(input())
b = int(input())
c = int(input())
if a > b and b > c and a > c:
    a,b,c = c,b,a
    print(a,b,c)
elif a < b and b > c and a < c:
    a,b,c = a,c,b
    print(a,b,c)
elif a < b and b > c and a > c:
    a,b,c = c,a,b
    print(a,b,c)
else:
    print(a,b,c)
# тут как-то просто перечислил все условия, можно было добавить числа в массив и сортануть?