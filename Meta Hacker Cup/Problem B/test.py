
with open("Problem B\input.txt") as file:
    x = file.readlines()
abc = []
for y in x:
    z = y.split("\n")[0]
    abc.append(z)

# print(abc)

# Function to determine if Alice has a guaranteed winning strategy
def has_winning_strategy(R, C, A, B):
    # If R or C is even, Alice wins
    if R % 2 == 0 and C % 2 == 0:
        return "NO"
    # If both R and C are odd, Alice loses
    else:
        return "YES"

# Read the number of test cases
T = int(abc[0])
# Process each test case
for case in range(1, T + 1):
    R, C, A, B = map(int, abc[case].split())
    result = has_winning_strategy(R, C, A, B)
    print(f"Case #{case}: {result}")
