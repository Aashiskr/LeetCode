#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        // Step 1: Sort the array to allow for a greedy approach
        sort(arr.begin(), arr.end());
        
        // Step 2: The first element must be 1
        arr[0] = 1;
        
        // Step 3: Iterate and enforce the rule: abs(arr[i] - arr[i - 1]) <= 1
        for (int i = 1; i < arr.size(); ++i) {
            arr[i] = min(arr[i], arr[i - 1] + 1);
        }
        
        // Step 4: The last element is guaranteed to be the maximum
        return arr.back();
    }
};