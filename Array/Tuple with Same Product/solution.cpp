class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> products;
        for(int i{}; i < n; ++i) {
            for(int j{i+1}; j < n; ++j) {
                products[nums[i] * nums[j]]++;
            }
        }

        int result{};
        for(int i{}; i < n; ++i) {
            for(int j{i+1}; j < n; ++j) {
                result += products[nums[i] * nums[j]] - 1;
            }
        }

        return result*4;
    }
};
