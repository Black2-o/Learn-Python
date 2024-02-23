# Function to check if it's possible to reach the goal and find the smallest possible apple weight
def find_smallest_apple_weight(N, weights):
    total_weight = sum(weights)
    
    # Check if it's possible to divide the total weight evenly over N days
    if total_weight % N == 0:
        return -1  # It's impossible to reach the goal
    
    # Calculate the desired weight for each day
    desired_weight_per_day = total_weight // N
    
    # Find the smallest possible additional apple weight
    smallest_apple_weight = min(weights)
    if smallest_apple_weight >= desired_weight_per_day:
        return smallest_apple_weight
    else:
        return desired_weight_per_day

# Read the number of test cases
T = int(input())

# Process each test case
for case in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    
    result = find_smallest_apple_weight(N, weights)
    
    print(f"Case #{case}: {result}")
