#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> nums;
        
        // 1. Flatten the 2D grid into a 1D vector
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                nums.push_back(grid[i][j]);
            }
        }
        
        // 2. Check if it's possible (All elements must have the same remainder modulo x)
        int remainder = nums[0] % x;
        for (int num : nums) {
            if (num % x != remainder) {
                return -1;
            }
        }
        
        // 3. Sort to find the median
        sort(nums.begin(), nums.end());
        int target = nums[nums.size() / 2]; // The median element
        
        // 4. Calculate total operations
        int totalOperations = 0;
        for (int num : nums) {
            totalOperations += abs(num - target) / x;
        }
        
        return totalOperations;
    }
};