class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int result{};
        for(int i{}, j{-1}; i < arr.size(); ++i) {
            j = max(j, arr[i]);
            if(i == j) {
                ++result;
                j = -1;
            }
        }
        return result;
    }
};
