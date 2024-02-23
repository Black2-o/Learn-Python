# Function to check if it's possible to reach the goal and find the smallest possible apple weight
def find_smallest_apple_weight(N, weights):
    total_weight = sum(weights)
    
    # Calculate the desired weight for each day
    desired_weight_per_day = total_weight // N

    run = True
    i = 1
    make_list = []
    while run:
        if N * i > total_weight:
            x = N * i
            make_list.append(x)
            run = False
        else:
            x = N * i
            make_list.append(x)
            i += 1
    return make_list
    # run_seven = True
    # i = 1
    # while run_seven:
    #     seven_multifly = 7 * i
    #     if desired_weight_per_day < seven_multifly:
    #         x = seven_multifly % desired_weight_per_day
    #         run_seven = False
    #     else:
    #         i += 1

    # need_more_weight = (desired_weight_per_day +x) * N - total_weight
    # # Find the smallest possible additional apple weight
    # smallest_apple_weight = min(weights)
    # if smallest_apple_weight >= desired_weight_per_day:
    #     return smallest_apple_weight
    # elif total_weight % N == 0:
    #     return -1
    # else:
    #     return need_more_weight

# Read the number of test cases
T = int(input())

# Process each test case
for case in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    
    result = find_smallest_apple_weight(N, weights)
    
    print(f"Case #{case}: {result}")
