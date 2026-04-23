class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        vector<long long> result(nums.size());
        unordered_map<int, vector<int>> num_to_idxs;
        for(int i = 0; i < nums.size(); ++i) {
            num_to_idxs[nums[i]].push_back(i);
        }
        for(auto &[num, idxs]: num_to_idxs) {
            long long s = accumulate(begin(idxs), end(idxs), 0LL);
            long long prefix = 0;
            long long m = idxs.size();
            for(long long i = 0; i < m; ++i) {
                long long idx = idxs[i];
                result[idx] = (s-prefix) - idx*(m-i) + idx*i-prefix;
                prefix += idx;
            }
        }
        return result;
    }
};
