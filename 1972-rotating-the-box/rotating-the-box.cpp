#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size();
        int n = boxGrid[0].size();
        
        // Step 1: Simulate gravity by pushing all stones to the right
        for (int i = 0; i < m; ++i) {
            int emptySpot = n - 1; // Keep track of the rightmost available space
            
            for (int j = n - 1; j >= 0; --j) {
                if (boxGrid[i][j] == '*') {
                    // Obstacle found, the next available space is right before it
                    emptySpot = j - 1;
                } else if (boxGrid[i][j] == '#') {
                    // Stone found, move it to the empty spot
                    boxGrid[i][j] = '.';
                    boxGrid[i][emptySpot] = '#';
                    emptySpot--; // Move the empty pointer one step to the left
                }
            }
        }
        
        // Step 2: Create a new grid to store the 90-degree rotated box
        vector<vector<char>> rotatedBox(n, vector<char>(m));
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rotatedBox[j][m - 1 - i] = boxGrid[i][j];
            }
        }
        
        return rotatedBox;
    }
};