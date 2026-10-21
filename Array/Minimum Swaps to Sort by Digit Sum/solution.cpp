class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> ns(n);
        for(int i = 0; i < n; ++i) {
            int num = nums[i];
            int s = 0;
            while(num) {
                s += num % 10;
                num /= 10;
            }
            ns[i] = {s, nums[i]};
        }
        ranges::sort(begin(ns), end(ns));
        int result = 0;
        unordered_map<int, int> goal_idxs;
        for(int i = 0; i < n; ++i) goal_idxs[ns[i].second] = i;
        vector<int> idxs(n);
        for(int i = 0; i < n; ++i) idxs[i] = goal_idxs[nums[i]];
        for(int i = 0; i < n; ++i) {
            while(idxs[i] != i) {
                int j = idxs[i];
                swap(idxs[i], idxs[j]);
                result++;
            }
        }
        return result;
    }
};
