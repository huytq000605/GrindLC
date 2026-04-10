class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int result = INT_MAX;
        unordered_map<int, pair<int, int>> idxs;
        for(int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if(idxs.find(num) == idxs.end()) {
                idxs[num] = {-1, i};
            } else {
                if(idxs[num].first != -1) result = min(result, (i - idxs[num].first) * 2);
                idxs[num] = {idxs[num].second, i};
            }
        }
        if(result == INT_MAX) return -1;
        return result;
    }
};
