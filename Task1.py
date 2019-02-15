print("Введите значение, определим, является ли строка записью числа")
a = input()
print(type(a))
if a.isdigit() == True:
    print("Является числом")
else:
    print("Строка содержит другие символы, кроме чисел")

print("Введите строку")
a = input()
a = a.count(' ')
print("Итого пробелов", a)

print("Введите строку")
a = input()
a = a.count('.')
print("Итого точек", a)

a = "Homework tz tz"
print(a.center(100, ' '))

a = "Homework tz tz"
print(a.title())