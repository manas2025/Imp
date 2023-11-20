import java.util.Scanner;

public class NQueensProblem {
    private int[] queens;        // Array to store the column positions of queens
    private int numSolutions;    // Count of solutions found
    private boolean foundSolution;  // Flag to stop after one solution is found

    // Constructor to initialize the N-Queens problem with the given size
    public NQueensProblem(int n) {
        queens = new int[n];
        numSolutions = 0;
        foundSolution = false;

        // Initialize the queens array with -1 to represent no queens initially
        for (int i = 0; i < n; i++) {
            queens[i] = -1;
        }
    }

    // Public method to start the solving process
    public void solve() {
        solveHelper(0);  // Start from the first row
    }

    // Recursive helper method to try placing queens in each row
    private void solveHelper(int row) {
        // Check if all queens are placed
        if (row == queens.length) {
            // Check if a solution hasn't been found yet
            if (!foundSolution) {
                numSolutions++;    // Increment the solution count
                printSolution();   // Print the current solution
                foundSolution = true;  // Set the flag to stop further solutions
            }
        } else {
            // Try placing a queen in each column of the current row
            for (int col = 0; col < queens.length; col++) {
                queens[row] = col;  // Place the queen in the current row and column
                if (isValid(row)) {
                    solveHelper(row + 1);  // Recursively move on to the next row
                }
            }
        }
    }

    // Check if placing a queen in the current position is valid
    private boolean isValid(int row) {
        // Check for conflicts with queens in previous rows
        for (int i = 0; i < row; i++) {
            if (queens[i] == queens[row] || Math.abs(queens[i] - queens[row]) == row - i) {
                return false;  // Conflict found, placement is not valid
            }
        }
        return true;  // No conflicts, placement is valid
    }

    // Print the current solution
    private void printSolution() {
        if (numSolutions == 1) {
            System.out.print("Solution: ");
        }
        // Print the column positions of queens in each row
        for (int i = 0; i < queens.length; i++) {
            System.out.print(queens[i] + " ");
        }
        System.out.println();  // Move to the next line

        // Print the matrix representation of the chessboard
        System.out.println("The Matrix Representation:");
        for (int i = 0; i < queens.length; i++) {
            for (int j = 0; j < queens.length; j++) {
                if (j == queens[i]) {
                    System.out.print("1 ");  // Queen placement
                } else {
                    System.out.print("0 ");  // Empty cell
                }
            }
            System.out.println();  // Move to the next line
        }
        System.out.println();  // Add an extra line for clarity
    }

    // Main method to take user input and solve the N-Queens problem
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter N for the N-Queens problem: ");
        int n = scanner.nextInt();

        // Create an instance of the NQueensProblem class
        NQueensProblem nQueensProblem = new NQueensProblem(n);
        nQueensProblem.solve();  // Solve the N-Queens problem
    }
}
