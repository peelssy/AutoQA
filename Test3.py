# a = input("Введите строку ")
# print(a[2], a[-2], a[0:5], a[:-2], a[0::2], a[1::2], a[::-1], a[-1::-2], a[-2:0:-1], len(a), sep='\n')
# a = input("Введите строку ")
# if len(a) % 2 == 0:
#     b = a[:int(len(a)/2)]
#     print(a[int(len(a)/2):]+b)
# else:
#     b = a[:int(len(a)/2+1)]
#     print(a[int(len(a)/2+1):]+b)
# x = 0
# while x <= 10:
#     print(x, end=' ')
#     x += 1
# x = 20
# while x >= 1:
#     print(x, end=' ')
#     x -= 1

# x = int(input())
# i = 0
# while x % 2 == 0:
#     x = x / 2
#     i += 1
# print(i)

l = [1, 2, 3, 4, 5, 6, 7, 8]
for a in l:
    l.remove(a)
    print(l)
