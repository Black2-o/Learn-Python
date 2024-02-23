# Function to determine if Alice has a guaranteed winning strategy
def has_winning_strategy(R, C, A, B):
    # If R or C is even, Alice wins
    if R % 2 == 0 and C % 2 == 0:
        return "NO"
    # If both R and C are odd, Alice loses
    else:
        return "YES"

# Read the number of test cases
T = input()
T = int(T)
# Process each test case
for case in range(1, T + 1):
    R, C, A, B = map(int, input().split())
    result = has_winning_strategy(R, C, A, B)
    print(f"Case #{case}: {result}")
