class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> A(nums.size(), 0);
        A[0] = 1;
        for(int i{}; i < nums.size() - 1; ++i) {
            if(((nums[i] ^ nums[i+1]) & 1) == 1) {
                A[i+1] = A[i] + 1;
            } else {
                A[i+1] = 1;
            }
        }
        
        vector<bool> result;
        for(auto &query: queries) {
            int a = query[0], b = query[1];
            result.emplace_back(b-a+1 <= A[b]);
        }
        return result;
    }
};
