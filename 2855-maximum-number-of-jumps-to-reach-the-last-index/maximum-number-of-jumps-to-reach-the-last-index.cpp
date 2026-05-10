#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        int n = nums.size();
        // dp[i] stores the maximum jumps to reach index i.
        // Initialize with -1 to indicate unreachable states.
        vector<int> dp(n, -1);
        
        // Base case: 0 jumps needed to reach the starting index
        dp[0] = 0; 
        
        for (int i = 0; i < n; ++i) {
            // If the current index is unreachable, we can't jump from it
            if (dp[i] == -1) continue;
            
            // Try jumping to all possible future indices j
            for (int j = i + 1; j < n; ++j) {
                // Use long long to prevent any potential integer overflow
                if (abs((long long)nums[j] - nums[i]) <= target) {
                    dp[j] = max(dp[j], dp[i] + 1);
                }
            }
        }
        
        // Return the max jumps to the last index (-1 if still unreachable)
        return dp[n - 1];
    }
};