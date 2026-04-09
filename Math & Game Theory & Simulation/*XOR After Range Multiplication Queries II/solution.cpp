class Solution {
    const int MOD = 1e9 + 7;
    long long power(long long base, long long exp) {
        long long result = 1;
        while(exp) {
            if(exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }

    long long mod_inv(long long num) {
        return power(num, MOD-2);
    }
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int sq = sqrt(n);
        // group queries with small k for later processing
        unordered_map<int, vector<vector<int>>> light_ks;
        for(auto &q: queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            if(k >= sq){ // large k: apply brute force
                for(int i = l; i <= r; i += k)
                    nums[i] = (1LL * nums[i] * v) % MOD;
            } else { // small k: process later
                light_ks[k].push_back(q);
            }
        }

        for(auto &[k, qs]: light_ks) {
            vector<long long> diff(n, 1);
            for(auto &q: qs) {
                int l = q[0], r = q[1], v = q[3];
                diff[l] = (diff[l] * v) % MOD;
                int inv_i = l + ((r-l)/k+1)*k;
                if(inv_i < n) diff[inv_i] = (diff[inv_i] * mod_inv(v)) % MOD;
            }

            for(int i = 0; i < n; ++i) {
                if(i >= k) diff[i] = (diff[i] * diff[i-k]) % MOD;
                nums[i] = (1LL * nums[i] * diff[i]) % MOD;
            }
        }
        
        int result = 0;
        for(int num: nums) result ^= num;
        return result;
    }
};
