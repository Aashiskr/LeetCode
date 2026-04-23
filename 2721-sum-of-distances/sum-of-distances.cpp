#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        vector<long long> res(n, 0);
        unordered_map<int, vector<int>> groups;

        // Group all indices by their value
        for (int i = 0; i < n; ++i) {
            groups[nums[i]].push_back(i);
        }

        // Process each group of indices
        for (auto& [val, indices] : groups) {
            int k = indices.size();
            if (k < 2) continue; // No other identical elements

            // Calculate total sum of indices in this group
            long long total_sum = 0;
            for (int idx : indices) {
                total_sum += idx;
            }

            long long prefix_sum = 0;
            for (int i = 0; i < k; ++i) {
                long long current_idx = indices[i];
                
                // Number of identical elements to the left and right
                long long left_count = i;
                long long right_count = k - 1 - i;
                
                // Sum of indices to the right
                long long suffix_sum = total_sum - prefix_sum - current_idx;

                // Apply the distance formula
                long long left_dist = (left_count * current_idx) - prefix_sum;
                long long right_dist = suffix_sum - (right_count * current_idx);

                res[current_idx] = left_dist + right_dist;

                // Update prefix sum for the next index in the group
                prefix_sum += current_idx;
            }
        }

        return res;
    }
};