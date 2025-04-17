class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> idxs;
        for(int i = 0; i < nums.size(); ++i) {
            idxs[nums[i]].emplace_back(i);
        }
        int result = 0;
        for(auto [_, is]: idxs) {
            unordered_map<int, int> gcd_counts;
            for(int i: is) {
                int gcdi = gcd(i, k);
                for(auto [gcdj, count]: gcd_counts) {
                    if((gcdi * gcdj) % k) continue;
                    result += count;
                }
                gcd_counts[gcdi]++;
            }
        }
        return result;
    }
};
