#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int, int>> q;
        
        q.push({0, 0});
        visited[0][0] = true;
        
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            
            // Reached the destination
            if (r == m - 1 && c == n - 1) {
                return true;
            }
            
            int curr = grid[r][c];
            
            // Check Right
            if (c + 1 < n && !visited[r][c + 1]) {
                int next = grid[r][c + 1];
                if ((curr == 1 || curr == 4 || curr == 6) && 
                    (next == 1 || next == 3 || next == 5)) {
                    visited[r][c + 1] = true;
                    q.push({r, c + 1});
                }
            }
            
            // Check Down
            if (r + 1 < m && !visited[r + 1][c]) {
                int next = grid[r + 1][c];
                if ((curr == 2 || curr == 3 || curr == 4) && 
                    (next == 2 || next == 5 || next == 6)) {
                    visited[r + 1][c] = true;
                    q.push({r + 1, c});
                }
            }
            
            // Check Left
            if (c - 1 >= 0 && !visited[r][c - 1]) {
                int next = grid[r][c - 1];
                if ((curr == 1 || curr == 3 || curr == 5) && 
                    (next == 1 || next == 4 || next == 6)) {
                    visited[r][c - 1] = true;
                    q.push({r, c - 1});
                }
            }
            
            // Check Up
            if (r - 1 >= 0 && !visited[r - 1][c]) {
                int next = grid[r - 1][c];
                if ((curr == 2 || curr == 5 || curr == 6) && 
                    (next == 2 || next == 3 || next == 4)) {
                    visited[r - 1][c] = true;
                    q.push({r - 1, c});
                }
            }
        }
        
        return false;
    }
};