class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        
        for (int i = 1; i <= n; ++i) {
            if (isGoodNumber(i)) {
                count++;
            }
        }
        
        return count;
    }
    
private:
    bool isGoodNumber(int num) {
        bool hasRotatableDiffDigit = false;
        
        while (num > 0) {
            int digit = num % 10;
            
            // If the number contains an invalid digit, it's not a good number
            if (digit == 3 || digit == 4 || digit == 7) {
                return false;
            }
            
            // If it contains a digit that changes upon rotation, mark it
            if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                hasRotatableDiffDigit = true;
            }
            
            num /= 10;
        }
        
        // It's a good number only if all digits are valid AND at least one digit changed
        return hasRotatableDiffDigit;
    }
};