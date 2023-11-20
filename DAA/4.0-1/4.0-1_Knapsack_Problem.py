# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
 
def knapSack(W, Wlist, Plist, N):
    k = [[0 for x in range(W + 1)] for x in range(N + 1)]
    
    # Build table k[][] in bottom up manner
    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif Wlist[i-1] <= w:
                k[i][w] = max(k[i-1][w-Wlist[i-1]] + Plist[i-1] , k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
 
    return k[N][W]
 
 
# Driver code
Plist = []
Wlist = []

N = int(input("Enter Number of Weight: "))
for i in range(N):
    Plist.append(int(input("Enter Profit: ")))
    Wlist.append(int(input("Enter Weight: ")))

W = int(input("\nEnter Max Weight: "))

print("\nProfit: ",Plist,"weight: ", Wlist)
print("\nMaximun Total Profit: ",knapSack(W, Wlist, Plist, N))