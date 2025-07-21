class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        unordered_map<int, vector<int>> idxs;
        for(int i = 0; i < nums.size(); ++i) {
            idxs[nums[i]].emplace_back(i);
        }
        vector<int> result;
        for(auto q: queries) {
            int num = nums[q];
            auto& positions = idxs[num];
            if(positions.size() == 1) {
                result.emplace_back(-1);
            } else {
                int i = lower_bound(positions.begin(), positions.end(), q) - positions.begin();

                int n = positions.size();
                int min_s = INT_MAX;
                for(int di: {-1, 1}) {
                    int s = abs(positions[i] - positions[(i+di+n)%n]);
                    s = min(s, static_cast<int>(nums.size()) - s);
                    min_s = min(min_s, s);
                }
                result.emplace_back(min_s);
            }
        }
        return result;
    }
};
