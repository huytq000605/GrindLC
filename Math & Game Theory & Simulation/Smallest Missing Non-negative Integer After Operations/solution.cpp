class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        unordered_map<int, int> um;
        for(int i = 0; i < nums.size(); ++i) {
            int mod = (nums[i] % value + value) % value;
            um[mod] += 1;
        }
        int result = INT_MAX;
        for(int v = 0; v < value; ++v) {
            result = min(result, um.find(v) == um.end() ? v: um[v] * value + v);
        }
        return result;
    }
};
