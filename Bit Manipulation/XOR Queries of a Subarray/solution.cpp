class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        for(int i = 1; i < arr.size(); i++) {
            arr[i] ^= arr[i-1];
        }
        vector<int> result;
        for(auto &q: queries) {
            int i = q[0], j = q[1];
            result.emplace_back(arr[j]);
            if(i) result.back() ^= arr[i-1];
        }
        return result;
    }
};
