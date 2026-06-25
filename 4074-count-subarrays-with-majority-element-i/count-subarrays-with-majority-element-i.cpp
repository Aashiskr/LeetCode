class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;

        BIT(int n) : n(n), bit(n + 1, 0) {}

        void add(int idx, int val) {
            for (; idx <= n; idx += idx & -idx)
                bit[idx] += val;
        }

        int sum(int idx) {
            int res = 0;
            for (; idx > 0; idx -= idx & -idx)
                res += bit[idx];
            return res;
        }
    };

    int countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();

        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (nums[i] == target ? 1 : -1);
        }

        vector<int> vals = pref;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());

        BIT bit(vals.size());

        long long ans = 0;

        for (int p : pref) {
            int idx = lower_bound(vals.begin(), vals.end(), p) - vals.begin() + 1;

            // Count previous prefix sums strictly smaller than p
            ans += bit.sum(idx - 1);

            bit.add(idx, 1);
        }

        return (int)ans;
    }
};