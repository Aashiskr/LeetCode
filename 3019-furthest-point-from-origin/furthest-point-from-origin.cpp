class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int net_fixed_distance = 0;
        int underscore_count = 0;
        
        for (char move : moves) {
            if (move == 'L') {
                net_fixed_distance--;
            } else if (move == 'R') {
                net_fixed_distance++;
            } else {
                underscore_count++;
            }
        }
        
        // Return absolute distance of fixed moves + all underscores in that direction
        return abs(net_fixed_distance) + underscore_count;
    }
};