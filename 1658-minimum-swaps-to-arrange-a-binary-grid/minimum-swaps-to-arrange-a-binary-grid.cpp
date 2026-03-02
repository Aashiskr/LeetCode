#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> trailing_zeros(n, 0);
        
        // Step 1: Pre-calculate trailing zeros for each row
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) {
                    count++;
                } else {
                    break;
                }
            }
            trailing_zeros[i] = count;
        }
        
        int total_swaps = 0;
        
        // Step 2: Greedy search and bubble-up
        for (int i = 0; i < n; i++) {
            int required_zeros = n - 1 - i;
            int found_idx = -1;
            
            // Find the nearest row that satisfies the requirement
            for (int j = i; j < n; j++) {
                if (trailing_zeros[j] >= required_zeros) {
                    found_idx = j;
                    break;
                }
            }
            
            // If no row can satisfy the requirement, the grid is invalid
            if (found_idx == -1) {
                return -1;
            }
            
            // Bubble the valid row up to the current position 'i'
            for (int k = found_idx; k > i; k--) {
                swap(trailing_zeros[k], trailing_zeros[k - 1]);
                total_swaps++;
            }
        }
        
        return total_swaps;
    }
};