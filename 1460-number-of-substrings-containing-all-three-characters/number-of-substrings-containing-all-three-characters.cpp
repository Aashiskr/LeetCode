class Solution {
public:
    int numberOfSubstrings(string s) {
        // Array to keep track of the most recent index of 'a', 'b', and 'c'
        int last_seen[3] = {-1, -1, -1};
        int count = 0;
        
        for (int i = 0; i < s.length(); ++i) {
            // Update the last seen index for the current character
            last_seen[s[i] - 'a'] = i;
            
            // If all three characters have been seen at least once
            if (last_seen[0] != -1 && last_seen[1] != -1 && last_seen[2] != -1) {
                // The number of valid substrings ending at 'i' is bounded by the minimum index
                count += min({last_seen[0], last_seen[1], last_seen[2]}) + 1;
            }
        }
        
        return count;
    }
};