class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> result;
        
        for (const string& q : queries) {
            for (const string& d : dictionary) {
                int diff = 0;
                // Since all words have the same length n
                for (int i = 0; i < q.length(); ++i) {
                    if (q[i] != d[i]) {
                        diff++;
                    }
                    // Optimization: if diff exceeds 2, this dictionary word won't work
                    if (diff > 2) break;
                }
                
                if (diff <= 2) {
                    result.push_back(q);
                    break; // Move to the next query once a match is found
                }
            }
        }
        
        return result;
    }
};