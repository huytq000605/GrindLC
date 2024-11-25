class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int lo{0}, hi = queries.size() + 1;
        while(lo < hi) {
            int k = lo + (hi - lo) / 2;
            vector<int> prefix(nums.size() + 1, 0);
            for(int i{}; i < k; ++i) {
                int a = queries[i][0], b = queries[i][1], c = queries[i][2];
                prefix[a] += c;
                prefix[b+1] -= c;
            }
            int cur{};
            bool valid{true};
            for(int i{}; i < nums.size(); ++i) {
                cur += prefix[i];
                if(nums[i] - cur > 0) {
                    valid = false;
                    break;
                }
            }
            
            if(!valid) lo = k+1;
            else hi = k;
        }
        return lo <= queries.size() ? lo : -1;
    }
};
