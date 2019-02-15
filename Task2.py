a = 179
b = 971
c = (a**2+b**2)**0.5
print("Гипотенуза", c)

print("Введите двузначное число")
a = int(input())
print("Число десятков", a//10%10)

print("введите трехзначное число")
a = input()
s = 0
for i in a:
    s += int(i)
print("сумма цифр", s)

print("введите число")
a = int(input())
if a % 2 == 0:
    print(a)
else:
    a += 1
    print(a)

print("введите число")
a = float(input())
a = a % 1
print(a)

print("введите число")
a = float(input())
a = int((a * 10) % 10)
print(a)

