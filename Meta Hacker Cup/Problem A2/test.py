

with open("Problem A2\input.txt") as file:
    x = file.readlines()
abc = []
for y in x:
    z = y.split("\n")[0]
    abc.append(z)
# print(abc)


# Create the function....
def largest_k_decker(single_Coast, dauble_coast, dolar_have, case_no):
    single_give_buns = 2
    dauble_give_buns = 2
    single_give_chease = 1
    dauble_give_chease = 2
    single_give_patis = 1
    dauble_give_patis = 2
    
    if case_no % 2 == 0 or case_no < 5:
        max_double_burgers = dolar_have // dauble_coast
        remaining_budget = dolar_have - (dauble_coast * max_double_burgers)
        single_burgers = remaining_budget // single_Coast
    else:
        single_burgers = dolar_have // single_Coast
        # remaining_budget = dolar_have - (single_Coast * single_burgers)
        max_double_burgers = 0



    total_buns = single_give_buns * single_burgers + dauble_give_buns * max_double_burgers
    total_cheese_slices = single_give_chease * single_burgers + dauble_give_chease * max_double_burgers
    total_patties = single_give_patis * single_burgers + dauble_give_patis * max_double_burgers

    if total_buns > 0:
        
        max_k = 1
        total_buns -= 2
        total_cheese_slices -= 1
        total_patties -= 1
        bun_checking = True
        while bun_checking:
            if total_buns >= 1 and total_cheese_slices >=1 and total_patties >= 1:
                max_k += 1
                total_buns -= 1
                total_cheese_slices -= 1
                total_patties -= 1
            else:
                bun_checking = False
        
    else:
        max_k = 0
    return max_k





# Read the number of test cases
T = int(abc[0])
# Process each test case
for case in range(1, T + 1):
    A, B, C = map(int, abc[case].split())
    D = case
    result = largest_k_decker(A, B, C, D)
    print(f"Case #{case}: {result}")
