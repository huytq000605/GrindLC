class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> result(n, 1);
        for(int i = 1; i < n; ++i) {
            if(ratings[i] > ratings[i-1]) {
                result[i] = result[i-1] + 1;
            }
        }
        for(int i = n-2; i >= 0; --i) {
            if(ratings[i] > ratings[i+1]) {
                result[i] = max(result[i], result[i+1] + 1);
            }
        }
        return accumulate(result.begin(), result.end(), 0);
    }
};
