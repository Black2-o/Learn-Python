# Function to check if you can build a K-decker cheeseburger
def can_build_k_decker(S, D, K):
    # Calculate the total number of buns, cheese slices, and patties
    total_buns = S + 2 * D
    total_cheese_slices = S + 1 * D
    total_patties = S + 1 * D
    
    # Check if you have enough ingredients to build a K-decker cheeseburger
    if total_buns >= K and total_cheese_slices >= K - 1 and total_patties >= K - 2:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = input()
T = int(T)
# Process each test case
for i in range(1, T + 1):
    S, D, K = map(int, input().split())
    result = can_build_k_decker(S, D, K)
    print(f"Case #{i}: {result}")
