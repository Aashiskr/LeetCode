#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return {};

        vector<int> max_left(n);
        vector<int> min_right(n);
        
        // max_left[i] stores the maximum value in nums[0...i]
        max_left[0] = nums[0];
        for (int i = 1; i < n; i++) {
            max_left[i] = max(max_left[i - 1], nums[i]);
        }
        
        // min_right[i] stores the minimum value in nums[i...n-1]
        min_right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            min_right[i] = min(min_right[i + 1], nums[i]);
        }
        
        vector<int> ans(n);
        int start = 0;
        
        // Find chunk boundaries and assign maximums
        for (int i = 0; i < n; i++) {
            // A boundary exists after index i if the maximum element in the 
            // current prefix is <= the minimum element in the remaining suffix.
            // (i == n - 1 ensures we close out the final chunk).
            if (i == n - 1 || max_left[i] <= min_right[i + 1]) {
                
                // For all elements in the current chunk [start...i],
                // the maximum reachable value is max_left[i].
                for (int j = start; j <= i; j++) {
                    ans[j] = max_left[i];
                }
                
                // Move the start pointer to the beginning of the next chunk
                start = i + 1;
            }
        }
        
        return ans;
    }
};