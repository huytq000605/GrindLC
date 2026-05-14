class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size() - 1;
        vector<int> counter(n+1);
        for(int num: nums) {
            if(num >= counter.size() || num < 1) return false;
            counter[num] += 1;
            if(counter[num] > 1 + (num == n)) return false;
        }
        return true;
    }
};
