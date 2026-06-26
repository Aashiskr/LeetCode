class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        
        // Since prefix sums can range from -n to n, we shift them to be strictly positive (1-indexed for BIT)
        int offset = n + 1;
        int max_val = 2 * n + 1;
        
        // Binary Indexed Tree (Fenwick Tree)
        vector<int> bit(max_val + 1, 0);
        
        // Helper to add 1 to the frequency of a given prefix sum
        auto add = [&](int idx, int val) {
            while (idx <= max_val) {
                bit[idx] += val;
                idx += idx & (-idx);
            }
        };
        
        // Helper to query the count of prefix sums strictly less than the current one
        auto query = [&](int idx) {
            long long sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & (-idx);
            }
            return sum;
        };
        
        long long ans = 0;
        int current_prefix = 0;
        
        // Insert the base case: a prefix sum of 0 before processing any elements
        add(current_prefix + offset, 1);
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                current_prefix += 1;
            } else {
                current_prefix -= 1;
            }
            
            // Count how many previous prefix sums were strictly smaller than current_prefix
            ans += query(current_prefix + offset - 1);
            
            // Add the current_prefix to the tree for future indices to use
            add(current_prefix + offset, 1);
        }
        
        return ans;
    }
};