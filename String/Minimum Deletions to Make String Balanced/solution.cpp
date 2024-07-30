class Solution {
public:
    int minimumDeletions(string s) {
        int ra = 0, rb = 0;
        for(auto c: s) {
            if(c == 'a') ra++;
            else rb++;
        }
        int result = min(ra, rb);
        int la = 0, lb = 0;
        for(auto c: s) {
            if(c == 'a') {
                la++;
                ra--;
            } else {
                lb++;
                rb--;
            }
            result = min(result, lb + ra);
        }
        return result;
    }
};
