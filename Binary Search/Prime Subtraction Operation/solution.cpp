class Solution {
inline static vector<bool> sieve{};
inline static vector<int> primes{0};
public:
    bool primeSubOperation(vector<int>& nums) {
        if(sieve.empty()) {
            sieve.resize(1000, true);
            sieve[1] = false;
            for(int i{2}; i <= 1000; ++i) {
                if(sieve[i]) {
                    int a = i * 2;
                    while(a <= 1000) {
                        sieve[a] = false;
                        a += i;
                    }
                    primes.emplace_back(i);
                }
            }
        }
        for(int i = 0; i < nums.size() - 1; ++i) {
            int lo = 0, hi = primes.size()-1;
            while(lo < hi) {
                int mid = lo + (hi - lo + 1) / 2;
                if(primes[mid] >= nums[i] || 
                    (i && nums[i] - primes[mid] <= nums[i-1])
                ) hi = mid-1;
                else lo = mid;
            }
            nums[i] -= primes[lo];
            if(nums[i] >= nums[i+1]) return false;
        }
        return true;
    }
};
