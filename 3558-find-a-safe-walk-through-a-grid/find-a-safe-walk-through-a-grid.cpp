#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Track the minimum health lost to reach each cell
        vector<vector<int>> min_damage(m, vector<int>(n, 1e9));
        deque<pair<int, int>> dq;
        
        // Starting point
        min_damage[0][0] = grid[0][0];
        dq.push_back({0, 0});
        
        // Directions: Up, Down, Left, Right
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        
        while(!dq.empty()) {
            auto [x, y] = dq.front();
            dq.pop_front();
            
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // Check boundaries
                if(nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    int damage = grid[nx][ny];
                    
                    // If we found a path with less damage to this cell
                    if(min_damage[x][y] + damage < min_damage[nx][ny]) {
                        min_damage[nx][ny] = min_damage[x][y] + damage;
                        
                        // 0-1 BFS logic: 
                        // 0-cost moves go to the front, 1-cost moves go to the back
                        if(damage == 0) {
                            dq.push_front({nx, ny});
                        } else {
                            dq.push_back({nx, ny});
                        }
                    }
                }
            }
        }
        
        // Check if the remaining health after taking the minimum possible damage is >= 1
        return (health - min_damage[m-1][n-1]) >= 1;
    }
};