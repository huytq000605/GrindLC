class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int result = 0;
        for(int c = 0; c < strs[0].size(); ++c) {
            bool sorted = true;
            for(int r = 0; r < strs.size()-1; ++r) {
                if(strs[r][c] > strs[r+1][c]) {
                    sorted = false;
                    break;
                }
            }
            result += !sorted;
        }
        return result;
    }
};
