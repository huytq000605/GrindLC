class Solution {
static constexpr int MOD = 1000000007;
public:
    int countOfPairs(vector<int>& nums) {
        map<pair<int, int>, int> dp; 
        auto dfs = [&](int i, int a1, auto dfs_ref) -> int {
            if(i >= nums.size()) return 1;
            if(dp.find({i, a1}) != dp.end()) return dp.find({i, a1})->second;
            int a2 = i > 0 ? nums[i-1] - a1 : 1001;
            int result = 0;
            for(int na1 = a1; na1 <= nums[i]; na1++) {
                int na2 = nums[i] - na1;
                if(a2 < na2) continue;
                int res = dfs_ref(i + 1, na1, dfs_ref);
                result = (result + res) % MOD;
            }
            dp.emplace(make_pair(make_pair(i, a1), result));
            return result;
        };
        
        return dfs(0, 0, dfs);
    }
};
