#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumLength(vector<int>& nums) {
        unordered_map<int, int> freq;
        
        // Step 1: Count the frequencies of all elements
        for (int num : nums) {
            freq[num]++;
        }
        
        int max_len = 1; // A single element is always a valid sequence of length 1
        
        // Step 2: Handle the special case where x = 1
        if (freq.count(1)) {
            int ones = freq[1];
            // The sequence must have an odd length. 
            // If the count of 1s is even, we have to leave one out.
            if (ones % 2 == 0) {
                ones--;
            }
            max_len = max(max_len, ones);
        }
        
        // Step 3: Iterate over the map to find chains for x > 1
        for (auto const& [x, count] : freq) {
            // Skip 1 as it's already handled
            if (x == 1) continue;
            
            int current_len = 0;
            long long curr = x;
            
            while (freq.count(curr) && freq[curr] > 0) {
                // If we have at least 2 of 'curr', we can extend both sides of the sequence
                if (freq[curr] >= 2) {
                    long long next_val = curr * curr;
                    
                    // Verify the next square actually exists in our array and doesn't exceed constraints
                    if (next_val <= 1e9 && freq.count(next_val) && freq[next_val] > 0) {
                        current_len += 2;
                        curr = next_val;
                    } else {
                        // The next square doesn't exist, so 'curr' is the peak
                        current_len += 1;
                        break;
                    }
                } else {
                    // We only have 1 of 'curr', so it must be the peak
                    current_len += 1;
                    break;
                }
            }
            
            // Update the global maximum length found
            max_len = max(max_len, current_len);
        }
        
        return max_len;
    }
};