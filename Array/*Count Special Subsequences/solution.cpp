class Solution {
public:
    long long numberOfSubsequences(vector<int>& nums) {
        int n = nums.size();
        long long result{};
        // p * r = q * s => p/q = s/r
        // every time we extend r, we have new pairs (q, p) with p = r-2
        unordered_map<double, int> counter;
        for(int r{4}; r < n; ++r) {
            int q{r-2};
            for(int p{}; p < q-1; ++p) {
                counter[static_cast<double>(nums[p]) / nums[q]]++;
            }
            for(int s{r+2}; s < n; ++s) {
                double target = static_cast<double>(nums[s]) / nums[r];
                if(counter.find(target) != counter.end()) {
                    result += counter[target];
                }
            }
        }
        return result;
    }
};
