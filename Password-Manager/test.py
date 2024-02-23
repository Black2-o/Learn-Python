# # with open("xyz.txt", "w") as file:
# #     file.write("Hello World!\n")
# #     file.write("Free Okey\n")

# with open("xyz.txt", "a") as file:
#     file.write("Hello xyz!\n")
#     file.write("Free xyz domain")
import json
with open("database.json", "r") as data:
    # Reading Old Data
    dataX = json.load(data)
    # Updating Old Data With new Data
    print(dataX)