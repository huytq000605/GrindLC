class Solution {
static inline vector<bool> is_prime;
public:
    vector<int> closestPrimes(int left, int right) {
        if(is_prime.empty()) {
            is_prime.resize(pow(10, 6) + 1, true);
            is_prime[0] = false;
            is_prime[1] = false;
            for(int i{2}; i <= pow(10, 6); ++i) {
                if(is_prime[i]) {
                    for(int j = i*2; j <= pow(10, 6); j+=i) is_prime[j] = false;
                }
            }
        }
        int prev = 0;
        vector<int> result{left, right+1};
        for(int num = max(2, left); num <= right; ++num) {
            if(is_prime[num]) {
                if(prev && num - prev < result[1] - result[0]) {
                    result = {prev, num};
                }
                prev = num;
            }
        }
        if(result[1] == right+1) return {-1, -1};
        return result;
    }
};
