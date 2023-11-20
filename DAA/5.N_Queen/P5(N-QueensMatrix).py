class NQueensProblem:
    def __init__(self, n):
        self.queens = [-1] * n
        self.numSolutions = 0
        self.found_solution = False  # Flag to stop after one solution is found

    def solve(self):
        self.solve_helper(0)

    def solve_helper(self, row):
        if row == len(self.queens):
            if not self.found_solution:  # Check if a solution hasn't been found yet
                self.numSolutions += 1
                self.print_solution()
                self.found_solution = True  # Set the flag to stop further solutions
        else:
            for col in range(len(self.queens)):
                self.queens[row] = col
                if self.is_valid(row):
                    self.solve_helper(row + 1)

    def is_valid(self, row):
        for i in range(row):
            if (
                self.queens[i] == self.queens[row]
                or abs(self.queens[i] - self.queens[row]) == row - i
            ):
                return False
        return True

    def print_solution(self):
        if self.numSolutions == 1:
            print("Solution:", end=" ")
        for i in range(len(self.queens)):
            print(self.queens[i], end=" ")
        print()
        print("The Matrix Representation:")
        for i in range(len(self.queens)):
            for j in range(len(self.queens)):
                if j == self.queens[i]:
                    print("1", end=" ")  # Queen placement
                else:
                    print("0", end=" ")  # Empty cell
            print()
        print()

if __name__ == "__main__":
    n = int(input("Enter N for the N-Queens problem: "))
    NQueensProblem = NQueensProblem(n)
    NQueensProblem.solve()

"""
Enter N for the N-Queens problem: 4
Solution: 1 3 0 2
The Matrix Representation:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

Enter N for the N-Queens problem: 8
Solution: 0 4 7 5 2 6 1 3
The Matrix Representation:
1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
"""