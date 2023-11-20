
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)

    finalvalue = 0.0
 
    print("\nprofit, weight: ",end=" ")
    for item in arr:
        if item.weight <= W:
            print([item.profit, item.weight], end=" ")

            W -= item.weight
            finalvalue += item.profit
        else:
            print([item.profit, item.weight], end=" ")
            
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue
 
 
# Driver's Code
if __name__ == "__main__":
    # Value and weight list
    Wlist = []
    wtN = int(input("Enter number of weights: "))
    
    for i in range(wtN):
        m  = int(input("Enter the Value of item: "))
        n  = int(input("Enter the Weight of item: "))
        Wlist.append(Item(m,n))
        
    W = int(input("\nEnter Max Weigth: "))
    
    # Function call
    result = fractionalKnapsack(W, Wlist)
    print ('\n\nMaximum profit we can obtain = ',result)


    