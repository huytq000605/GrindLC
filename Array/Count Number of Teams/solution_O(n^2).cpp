class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int result = 0;
        for(int j = 1; j < n-1; ++j) {
            int lt = 0, gt = 0;
            for(int i = 0; i < j; ++i) {
                lt += rating[i] < rating[j];
                gt += rating[i] > rating[j];
            }
            for(int k = j+1; k < n; ++k) {
                if(rating[k] > rating[j]) result += lt;
                if(rating[k] < rating[j]) result += gt;
            }
        }
        return result;
    }
};
