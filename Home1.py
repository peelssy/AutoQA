# def enter_word():
#     while True:
#         s = input("Enter word: ").strip()
#         if s.isalpha():
#             return s
# word = enter_word()
# assert word.isalpha()

# def word_printer(word, count=1, wow=0):
#     if wow == 1:
#         return (word * count).upper()
#     else:
#         return word * count
#
# print(word_printer(wow=1, 'Bob'))

# def premax(*numbers):
#     l = list(numbers)
#     l.sort()
#     return l[-2]
# print(premax(6,2,3,1))
#
# def f(a, b, *ll):
#     print(a + b)
#     print(sum(ll))
#
# f(1, 2, 1, 1, 1)

def func(**kwargs):
    return '{} is {}'.format(kwargs.get('name'), kwargs.get('job'))

print(func(a=1, job='lazy', name='Bob'))

