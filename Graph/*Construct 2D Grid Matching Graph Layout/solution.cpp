class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int mxx = *max_element(nums.begin(), nums.end());
        vector<int> divisors(mxx+1, 0);
        for(int num: nums) {
            for(int i = 1; i * i <= num; ++i) {
                if(num % i) continue;
                ++divisors[i];
                if(i != num / i) ++divisors[num / i];
            }
        }
        vector<long long> gcd_count(mxx+1, 0);
        for(int i = mxx; i >= 1; --i) {
            gcd_count[i] = static_cast<long long>(divisors[i]) * (divisors[i]-1) / 2; // C(n, 2)
            for(long long mul = 2; i * mul <= mxx; ++mul) {
                gcd_count[i] -= gcd_count[i*mul];
            }
        }

        vector<long long> pref(mxx+1, 0);
        for(int i = 1; i <= mxx; ++i) {
            pref[i] = pref[i-1];
            pref[i] += gcd_count[i];
        }
        vector<int> result;
        for(auto q: queries) {
            long long lo = 0, hi = mxx;
            while(lo < hi) {
                long long mid = lo + (hi - lo) / 2;
                if(pref[mid] <= q) lo = mid + 1;
                else hi = mid;
            }
            result.emplace_back(lo);
        }
        return result;
    }
};
