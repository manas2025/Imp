# Getting input from the user
n = int(input("Enter no. of items: "))
maxwt = int(input("Maximum weight: "))
profits = list(map(int, input("Enter profit value of items: ").split()))
weights = list(map(int, input("Enter weight of items: ").split()))

# Define a function to solve the 0-1 Knapsack problem using DP and Branch and Bound
def knapsack_dp_branch_bound(n, maxwt, profits, weights):
    # Initialize the memoization table
    dp = [[0 for _ in range(maxwt + 1)] for _ in range(n + 1)]

    # Initialize a priority queue for the branch and bound algorithm
    pq = []

    # Push the initial state (0 items, 0 weight, 0 profit, and upper bound)
    pq.append((0, 0, 0, 0))

    max_profit = 0

    while pq:
        items, weight, profit, bound = pq.pop()

        if weight > maxwt:
            continue

        if profit > max_profit:
            max_profit = profit

        if items == n:
            continue

        item_weight = weights[items]
        item_profit = profits[items]

        # Calculate the upper bound for the current node
        remaining_weight = maxwt - weight
        upper_bound = profit + bound

        # Consider taking the current item
        if weight + item_weight <= maxwt:
            pq.append((items + 1, weight + item_weight, profit + item_profit, upper_bound))

        # Calculate the upper bound for the child node if the item is not taken
        bound = upper_bound - (profit - item_profit) * (remaining_weight / item_weight)

        # Consider not taking the current item
        if bound > max_profit:
            pq.append((items + 1, weight, profit, bound))

    return max_profit

print("Item\tProfit\tBranch & Bound")
for i in range(n):
    profit_i = knapsack_dp_branch_bound(i + 1, maxwt, profits[:i + 1], weights[:i + 1])
    print(f"{i + 1}\t{profits[i]}\t{profit_i}")

"""
Enter no. of items: 5
Maximum weight: 10  
Enter profit value of items: 10 15 10 12 8
Enter weight of items: 3 3 2 5 1
Item    Profit  Branch & Bound
1       10      10
2       15      25
3       10      35
4       12      37
5       8       43
"""