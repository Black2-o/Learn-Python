'''
List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehension
'''

list_1 = [1, 5, 6, 11, 3, 9, 8,  7, 56, 45, 99, 43, 18, 27, 30, 11]
divide_by_3 = []
for x in list_1:
    if x % 3 == 0:
        divide_by_3.append(x)


print(divide_by_3)
divide_by_3_com = [x for x in list_1 if x % 3 == 0]
print(divide_by_3_com)


dict1 = {'a': 45, 'b': 55, 'c': 5, 'A': 20}
print(dict1.keys())
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0)
      for k in dict1.keys()})
squred = {x**2 for x in [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 5]}
print(squred)


gen = (i for i in range(50) if i % 3 == 0)
for i in gen:
    print(i)
