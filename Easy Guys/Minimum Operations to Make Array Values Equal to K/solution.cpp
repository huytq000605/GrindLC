class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int mn = *min_element(nums.begin(), nums.end());
        if(k > mn) return -1;
        return unordered_set(nums.begin(), nums.end()).size() - (mn == k);
    }
};
