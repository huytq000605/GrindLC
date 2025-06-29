class Solution {
int MOD = 1e9 + 7;
public:
    int numSubseq(vector<int>& nums, int target) {
        int n = nums.size();
        int result = 0;
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> counter(mx+1);
        for(int num: nums) counter[num]++;
        for(int mn = 0; mn <= mx;) {
            if(!counter[mn]) {++mn; continue;}
            while(mn <= mx && (mn + mx > target || !counter[mx])) {
                n -= counter[mx--];
            }
            if(mn > mx) break;
            result = (result + powmod(2, n-1)) % MOD;
            --n;
            --counter[mn];
        }
        return result;
    }

    int powmod(long long base, int exp) {
        if(!exp) return 1;
        long long result = 1;
        while(exp > 1) {
            if(exp & 1) result = (result * base) % MOD;
            exp >>= 1;
            base = (base * base) % MOD;
        }
        return (result * base) % MOD;
    }
};
