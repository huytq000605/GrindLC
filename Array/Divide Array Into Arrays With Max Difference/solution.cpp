class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> freq(mx+1);
        for(int &num: nums) ++freq[num];
        vector<vector<int>> result(n/3, vector<int>(3));
        for(int i = 0, num = 0; i < n / 3; ++i) {
            for(int j = 0; j < 3; ++j) {
                while(!freq[num]) ++num;
                if(j && num - result[i][0] > k) return {};
                result[i][j] = num;
                --freq[num];
            }
        }
        return result;
    }
};
