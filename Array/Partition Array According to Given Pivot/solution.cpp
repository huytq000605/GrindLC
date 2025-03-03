class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        int left = 0, right = n-1;
        vector<int> result(n);
        for(int i = 0; i < n; ++i) {
            if(nums[i] < pivot) {
                result[left] = nums[i];
                ++left;
            }
        }
        for(int i = n-1; i >= 0; --i) {
            if(nums[i] > pivot) {
                result[right] = nums[i];
                --right;
            }
        }
        while(left <= right) result[left++] = pivot;
        return result;
    }
};
