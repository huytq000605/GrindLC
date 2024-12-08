class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        long long total = accumulate(nums.begin(), nums.end(), 0);
        unordered_map<int, int> m;
        for(int num: nums) ++m[num];
        int result{-1002};
        for(int num: nums) {
            long long d = total - num;
            if((d & 1) == 0 && m.find(d / 2) != m.end() && (d/2 != num || m[num] > 1)) result = max(result, num);
        }
        return result;
    }
};
