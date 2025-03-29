vector<int> prime_scores(100001, 0);
class Solution {
    int MOD = pow(10, 9) + 7;
    int prime_score(int num) {
        if(prime_scores[num]) return prime_scores[num];
        int original = num;
        int result = 0;
        int bound = sqrt(num);
        for(int factor = 2; factor <= bound; ++factor) {
            int s = 0;
            while(num % factor == 0) {
                num /= factor;
                s = 1;
            }
            result += s;
        }
        result += num > 1;
        return prime_scores[original] = result;
    }

    long long pow_mod(long long base, int exp) {
        if(exp == 0) return 1;
        long long p = pow_mod(base, exp / 2);
        p = (p * p) % MOD;
        if(exp & 1) p *= base;
        return p % MOD;
    }
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> scores(n);
        for(int i = 0; i < n; ++i) {
            scores[i] = prime_score(nums[i]);
        }

        vector<int> st;
        vector<int> gt_right(n, n), gte_left(n, -1);
        for(int i = 0; i < n; ++i) {
            while(!st.empty() && scores[st.back()] < scores[i]) {
                int j = st.back(); st.pop_back();
                gt_right[j] = i;
            }
            if(!st.empty()) gte_left[i] = st.back();
            st.emplace_back(i);
        }
        
        vector<pair<int, int>> inums(n);
        for(int i = 0; i < n; ++i) {
            inums[i] = {i, nums[i]};
        }
        sort(inums.begin(), inums.end(), [](auto &p1, auto &p2) {
            return p1.second > p2.second;
        });
        long long result = 1;
        for(auto [i, num]: inums) {
            
            int right = gt_right[i];
            int left = gte_left[i];
            long long t = min(static_cast<long long>(k), static_cast<long long>(right - i) * (i - left));
            k -= t;
            result = (result * pow_mod(num, t)) % MOD;
            if(!k) break;
        }
        return result;  
    }
};
