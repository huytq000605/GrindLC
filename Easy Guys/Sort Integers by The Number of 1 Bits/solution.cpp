class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(begin(arr), end(arr));
        vector<vector<int>> bits(14);
        for(int num: arr) {
            bits[popcount(static_cast<uint>(num))].push_back(num);
        }
        vector<int> result;
        for(auto &arr: bits) {
            for(auto num: arr) {
                result.push_back(num);
            }
        }
        return result;
    }
};
