#include <vector>

using namespace std;

class Solution {
    int MOD = 1e9 + 7;
    typedef vector<vector<int>> matrix;

    // Helper function to multiply two matrices
    matrix mul(const matrix& A, const matrix& B) {
        int n = A.size();
        int m = B[0].size();
        int p = B.size();
        matrix C(n, vector<int>(m, 0));
        
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < p; k++) {
                if (A[i][k] == 0) continue; // Skip zero multipliers to optimize
                for (int j = 0; j < m; j++) {
                    C[i][j] = (C[i][j] + 1LL * A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    // Helper function for matrix exponentiation
    matrix power(matrix A, int p) {
        int n = A.size();
        matrix res(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) res[i][i] = 1; // Identity matrix
        
        while (p > 0) {
            if (p & 1) res = mul(res, A);
            A = mul(A, A);
            p >>= 1;
        }
        return res;
    }

public:
    int zigZagArrays(int n, int l, int r) {
        int k = r - l + 1;
        int S = 2 * k;

        // Base state vector V2 for sequence of length 2
        // Indices 0 to k-1 represent "UP" states
        // Indices k to 2k-1 represent "DOWN" states
        matrix V2(S, vector<int>(1, 0));
        for (int v = 0; v < k; ++v) {
            V2[v][0] = v;                   // Ends at v+1 going UP (needs a smaller preceding element)
            V2[v + k][0] = k - (v + 1);     // Ends at v+1 going DOWN (needs a larger preceding element)
        }

        // Transition matrix T
        matrix T(S, vector<int>(S, 0));
        
        // Transitions from UP state (must go to DOWN)
        for (int j = 0; j < k; ++j) { 
            int val_prev = j + 1;
            for (int i = k; i < S; ++i) { 
                int val_next = i - k + 1;
                if (val_next < val_prev) {
                    T[i][j] = 1;
                }
            }
        }
        
        // Transitions from DOWN state (must go to UP)
        for (int j = k; j < S; ++j) { 
            int val_prev = j - k + 1;
            for (int i = 0; i < k; ++i) { 
                int val_next = i + 1;
                if (val_next > val_prev) {
                    T[i][j] = 1;
                }
            }
        }

        // Calculate (T ^ (n-2)) * V2
        matrix Tn = power(T, n - 2);
        matrix Vn = mul(Tn, V2);

        // Sum up all possible ending states
        long long ans = 0;
        for (int i = 0; i < S; ++i) {
            ans = (ans + Vn[i][0]) % MOD;
        }

        return ans;
    }
};