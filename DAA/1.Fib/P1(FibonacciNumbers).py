print("\nFibonacci using Recursion")
n = int(input("Enter number of terms:"))
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    

print("\nFibonacci using Non-Recursion")
print("Fibonacci sequence:")
#for i in range(n):
    #print(fibonacci(i))

a = int(input("Enter the first number of the series: "))
b = int(input("Enter the second number of the series: "))
num = int(input("Enter the number of terms needed: "))
print("Fibonacci sequence: ")
print(a, b, end=" ")

while (num - 2):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    num = num - 1


"""
Fibonacci using Recursion
Enter number of terms:4

Fibonacci using Non-Recursion
Fibonacci sequence:
0
1
1
2
Enter the first number of the series: 0
Enter the second number of the series: 1
Enter the number of terms needed: 10
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34
"""