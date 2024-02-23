# Syntaz:-
# {key: value for (key, value) in iterable}

nums = [1, 2, 3, 4, 5]
# output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# my_dict = {}

# for num in nums:
#     my_dict[num] = num**2
# print(my_dict)

# my_dict1 = {num: num**2 for num in nums}
# print(my_dict1)


# my_dict = {}

# for num in nums:
#     if num % 2 == 0:
#         my_dict[num] = num**2
# print(my_dict)

# my_dict1 = {num: num**2 for num in nums if num % 2 == 0}
# print(my_dict1)


# Example 2:

star1 = "cOdINg"
my_dict = {}
for char in star1:
    my_dict[char.upper()] = (ord(char), ord(char.swapcase()))
print(my_dict)

my_dict1 = {char.upper(): (ord(char), ord(char.swapcase())) for char in star1}
print(my_dict1)
