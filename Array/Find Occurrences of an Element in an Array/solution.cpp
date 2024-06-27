class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        vector<int> idxs;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == x) {
                idxs.emplace_back(i);
            }
        }
        vector<int> result;
        for(int query: queries) {
            if(query > idxs.size()) result.emplace_back(-1);
            else result.emplace_back(idxs[query-1]);
        }
        return result;
    }
};
