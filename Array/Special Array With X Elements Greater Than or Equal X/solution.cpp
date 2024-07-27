class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend());
        int n = nums.size();
        int i = 0;
        for(int x = n; x >= 0; x--) {
            while(i < n && nums[i] >= x) {
                i++;
            }
            if(i == x) return x;
        }
        return -1;
    }
};class Solution {
