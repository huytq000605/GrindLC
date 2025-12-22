class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int result = 0;
        vector<bool> is_valid(n, false);
        for(int i = 0; i < strs[0].size(); ++i) {
            bool valid = true;
            for(int j = 0; j < n-1; ++j) {
                if(!is_valid[j] && strs[j][i] > strs[j+1][i]) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                for(int j = 0; j < n-1; ++j) {
                    is_valid[j] = is_valid[j] || (strs[j][i] < strs[j+1][i]); 
                }
            } else {
                result++;
            }
        }
        return result;
    }
};
