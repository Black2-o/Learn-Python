with open("camo.txt") as file:
    x=file.readlines()

# print(x)

main_list = []

for first in x:
    z = (((first.split("\n")[0]).split(":- ")))
    try:
        main = z[1]
    except:
        main = "\n"

    main_list.append(main)

a = "\n"
b = 0
i = 2
j = 3
for main_loop in main_list:
    if b == i or b == j:
        final = a + main_loop
        if b == i:
            i += 4
        elif b == j:
            j += 4
    else:
        final = a + main_loop + ":"
    a = final
    b += 1



with open("output.txt", "a") as file:
    file.write(final)