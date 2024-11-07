class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int result = 0;
        for(int i{0}; i < 32; ++i) {
            int res = 0;
            for(int num: candidates) {
                if((num >> i) & 1) ++res;
            }
            result = max(result, res);
        }
        return result;
    }
};
