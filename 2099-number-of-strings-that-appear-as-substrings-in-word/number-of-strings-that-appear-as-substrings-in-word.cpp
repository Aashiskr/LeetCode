class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int count = 0;
        
        for (const string& pattern : patterns) {
            // string::find returns string::npos if the substring is not found
            if (word.find(pattern) != string::npos) {
                count++;
            }
        }
        
        return count;
    }
};