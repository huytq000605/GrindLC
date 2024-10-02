class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        int freq[1001], result = -1;
        for(auto num: nums) ++freq[num];
        for(auto num: nums) if(freq[num] == 1) result = max(result, num);
        return result;
    }
};
