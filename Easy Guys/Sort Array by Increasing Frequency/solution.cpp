class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> counter;
        for(auto num: nums) counter[num] += 1;
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            return counter[a] == counter[b] ? a > b : counter[a] < counter[b];
        });
        return nums;
    }
};
