class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        long long result = 0;
        for(int i = 0, j = 0; i < prices.size(); ++i) {
            if(i && prices[i] != prices[i-1] - 1) {
                j = i;
            }
            result += (i - j + 1);
        }
        return result;
    }
};
