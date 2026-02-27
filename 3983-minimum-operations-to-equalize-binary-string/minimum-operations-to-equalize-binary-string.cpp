class Solution {
public:
    int minOperations(string s, int k) {
        int n = s.length();
        int c = 0;
        
        // Count initial number of '0's
        for (char ch : s) {
            if (ch == '0') c++;
        }
        
        // Agar pehle se hi saare '1' hain
        if (c == 0) return 0; 

        // L = minimum possible zeros, R = maximum possible zeros
        int L = c, R = c;
        
        // Shortest path n steps se zyada nahi ho sakta
        for (int step = 1; step <= n; ++step) {
            int next_L, next_R;

            // Next step ke liye MINIMUM zeros calculate karo
            if (L <= k && k <= R) {
                // Parity check (even/odd logic)
                next_L = (L % 2 == k % 2) ? 0 : 1; 
            } else if (k < L) {
                next_L = L - k;
            } else { // k > R
                next_L = k - R;
            }

            // Next step ke liye MAXIMUM zeros calculate karo
            if (L <= n - k && n - k <= R) {
                next_R = (L % 2 == (n - k) % 2) ? n : n - 1;
            } else if (n - k < L) {
                next_R = 2 * n - (L + k);
            } else { // n - k > R
                next_R = R + k;
            }

            // Agar kisi bhi point pe minimum zeros 0 ho gaye, kaam khatam!
            if (next_L == 0) return step;

            // Range update karo next loop ke liye
            L = next_L;
            R = next_R;
        }

        return -1; // Agar saare possible steps mein target nahi mila
    }
};