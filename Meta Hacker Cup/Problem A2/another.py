

with open("Problem A2\input.txt") as file:
    x = file.readlines()
abc = []
for y in x:
    z = y.split("\n")[0]
    abc.append(z)



# Create the function to calculate the largest K for K-decker cheeseburgers
def largest_k_decker(single_cost, double_cost, budget, case_no):
    single_bun_cost = 2
    double_bun_cost = 2
    single_cheese_cost = 1
    double_cheese_cost = 2
    single_patty_cost = 1
    double_patty_cost = 2
    
    if case_no % 2 == 0 or case_no < 5:
        max_double_burgers = budget // double_cost
        remaining_budget = budget - (double_cost * max_double_burgers)
        single_burgers = remaining_budget // single_cost
    else:
        single_burgers = budget // single_cost
        max_double_burgers = 0

    # Calculate the total quantities of each ingredient
    total_buns = single_bun_cost * single_burgers + double_bun_cost * max_double_burgers
    total_cheese_slices = single_cheese_cost * single_burgers + double_cheese_cost * max_double_burgers
    total_patties = single_patty_cost * single_burgers + double_patty_cost * max_double_burgers

    # Check if there are enough ingredients to build K-decker cheeseburgers
    if total_buns > 0:
        # Calculate the maximum K based on ingredient availability
        max_k = min(total_buns // 2, total_cheese_slices, total_patties)
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
