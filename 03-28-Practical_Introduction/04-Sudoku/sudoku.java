import java.util.HashSet;
import java.util.Set;

// Time Complexity: O(N^2)
// where N is the dimension of the matrix

// Space Complexity: O(N^2)
// where N is the dimension of the matrix

class Solution {
    public boolean isValidSudoku(char[][] board) {
    Set seen = new HashSet<>();
    for (int i=0; i<9; ++i) {
        for (int j=0; j<9; ++j) {
            char number = board[i][j];
            // If the position is a number (!= '.'),
            // then we can try adding the number and its information into the HashSet.
            if (number != '.')
                // The HashSet.add() function returns a boolean result, true if added successfully and false otherwise.
                // As such, we can just use this boolean return from add() to check if we successfully added.
                // If any of the 3 (row, column and box) is not added successfully,
                // then 'board' is not a valid sudoku board.
                // 1. Store the number in the row.
                // 2. Store the number in the column.
                // 3. Store the number in the box. (Make sure to separate row and column information with a delimiter).
                if (!seen.add(number + " in row " + i) ||
                    !seen.add(number + " in column " + j) ||
                    !seen.add(number + " in block " + i/3 + "," + j/3))
                    return false;
        }
    }

    // If all checks succeed, then the 'board' is a valid sudoku.
    return true;
}
}