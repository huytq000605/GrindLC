class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> pairs, triplets;
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            for(int j = i; j < n; ++j) {
                pairs.insert(nums[i] ^ nums[j]);
            }
        }
        for(int xy: pairs) {
            for(int z: nums) {
                triplets.insert(xy ^ z);
            }
        }
        return triplets.size();
    }
};
