class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int mx = nums[0][0];
        priority_queue<tuple<int, int, int>,
            vector<tuple<int, int, int>>,
            decltype([](auto &t1, auto &t2) -> bool {
                return get<0>(t1) > get<0>(t2);
            })> pq;
        for(int i = 0; i < nums.size(); ++i) {
            mx = max(mx, nums[i][0]);
            pq.emplace(nums[i][0], i, 0);
        }
        auto result = vector<int>{get<0>(pq.top()), mx};
        while(pq.size() == nums.size()) {
            auto [mn, l, i] = pq.top();
            if(mx - mn < result[1] - result[0]) result = {mn, mx};
            pq.pop();
            if(i+1 < nums[l].size()) {
                pq.emplace(nums[l][i+1], l, i+1);
                mx = max(mx, nums[l][i+1]);
            }
        }
        return result;
    }
};
