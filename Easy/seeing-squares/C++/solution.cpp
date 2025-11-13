// Written by Joseph Garcia

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int rows;
    int cols;
    cin >> rows >> cols; 
    cin.ignore();
  
    vector<string> grid(rows);
    for (int i = 0; i < rows; i++) {
        string row;
        getline(cin, row);

        // Ensure Row has exactly c characters.
        if ((int)row.size() < cols){
            row += string(cols - row.size(), ' ');
        } else if ((int)row.size() > cols) {
            row = row.substr(0, cols);
        }
        grid[i] = row;
    }

    // Precompute horizontal_runs of '-' or '+'.
    vector<vector<int>> horizontal_run(rows, vector<int>(cols, 0));
    for (int r = 0; r < rows; ++r) {
        for (int c = cols - 1; c >= 0; --c) {
            char ch = grid[r][c];
            if (ch == '-' || ch == '+') {
                if (c + 1  < cols) horizontal_run[r][c] = 1 + horizontal_run[r][c + 1];
                else horizontal_run[r][c] = 1;     
            } else {
                horizontal_run[r][c] = 0;
            }
        }
    }

    // Precompute vertical_runs of '|' or '+'.
    vector<vector<int>> vertical_run(rows, vector<int>(cols, 0));
    for (int c = 0; c < cols; ++c) {
        for (int r = rows - 1; r >= 0; --r) {
            char ch = grid[r][c];
            if (ch == '|' || ch == '+') {
                if (r + 1 < rows) vertical_run[r][c] = 1 + vertical_run[r + 1][c];
                else vertical_run[r][c] = 1;
            } else {
                vertical_run[r][c] = 0;
            }
        }
    }

    long long count_squares = 0;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] != '+') continue;

            // Try all possible heights h >= 2
            for (int h = 2; ;++h) {
                int bottom_row = r + h - 1;

                // Horizontal distance from '+' to '+'
                int w = 2 * (h - 1);
                int right_col = c + w;
                
                // Handle out of bounds.
                if (bottom_row >= rows || right_col >= cols) break;

                int r2 = bottom_row;
                int c2 = right_col;

                // Check corners are '+'
                if (grid[r][c2] != '+' ||
                    grid[r2][c] != '+' ||
                    grid[r2][c2] != '+')
                    continue;

                // Check top side (row r from c to c2) is all '-' or '+'
                if (horizontal_run[r][c] < w + 1) continue;

                // Check bottom side (row r2 from c to c2)
                if (horizontal_run[r2][c] < w + 1) continue;

                // Check left side (col c fro r to r2) is all '|' or '+'
                if (vertical_run[r][c] < h) continue;

                // Check right side (col c2 from r to r2)
                if (vertical_run[r][c2] < h) continue;

                // Valid square found!
                ++count_squares;
            }
        }
    }
    cout << count_squares << endl;
}
