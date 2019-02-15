print("введите три числа")
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a != b == c or a == b != c or c != a == b:
    print(2)
else:
    print(0)

d = {}
d['name'] = 'Vasya'
d['age'] = 20
d['age'] += 1
print(d['age'])
d['profession'] = 'enginner'
print(d)
d['profession'] = 'racer'
print(d)
