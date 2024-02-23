# try:
#     file = open("a_file.txt")
#     a_dictionary = {"Key": "Value"}
#     print(a_dictionary["Key"])#["adfa"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} Doesn't exist.")

# else:
#     content = file.read()
#     print(content)
# finally:
#     # raise KeyError
#     raise TypeError("this is a type error")
#     # file.close()
#     # print("File was closed.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("HUman Height should not be over 3 meters.10")

bmi = weight / height ** 2 
print(bmi)