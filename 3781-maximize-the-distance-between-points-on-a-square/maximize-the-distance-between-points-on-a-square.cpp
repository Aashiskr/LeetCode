#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        vector<long long> A(n);
        
        // 1. Map 2D boundary coordinates to a 1D perimeter line
        for (int i = 0; i < n; ++i) {
            long long x = points[i][0];
            long long y = points[i][1];
            if (y == 0) {
                A[i] = x;                               // Bottom edge
            } else if (x == side) {
                A[i] = side + y;                        // Right edge
            } else if (y == side) {
                A[i] = 2LL * side + (side - x);         // Top edge
            } else {
                A[i] = 3LL * side + (side - y);         // Left edge
            }
        }
        
        sort(A.begin(), A.end());
        
        // 2. Handle circular wrap-around by doubling the array length
        long long L = 4LL * side;
        vector<long long> B(2 * n);
        for (int i = 0; i < n; ++i) {
            B[i] = A[i];
            B[i + n] = A[i] + L;
        }
        
        // 3. Binary Search for the optimal maximum-minimum distance
        long long low = 1, high = side; 
        long long ans = 0;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (check(mid, B, n, k, L)) {
                ans = mid;         // Mid is valid, try to find a larger distance
                low = mid + 1;
            } else {
                high = mid - 1;    // Mid is too large, scale back
            }
        }
        
        return ans;
    }
    
private:
    bool check(long long d, const vector<long long>& B, int n, int k, long long L) {
        // Precompute the next valid point that is at least 'd' distance away
        int r = 0;
        vector<int> next_idx(2 * n + 1, 2 * n);
        for (int l = 0; l < 2 * n; ++l) {
            while (r < 2 * n && B[r] - B[l] < d) {
                r++;
            }
            next_idx[l] = r;
        }
        
        // Check if there is any valid starting point that satisfies the condition for 'k' points
        for (int i = 0; i < n; ++i) {
            int curr = i;
            int steps = 1;
            
            // Greedily jump to the next valid point
            while (steps < k && curr < 2 * n) {
                curr = next_idx[curr];
                steps++;
            }
            
            // If we successfully picked 'k' points, ensure the wrap-around distance is also >= d
            // Distance from last point to start point: L - (B[curr] - B[i]) >= d
            if (steps == k && curr < 2 * n && B[curr] - B[i] <= L - d) {
                return true;
            }
        }
        
        return false;
    }
};