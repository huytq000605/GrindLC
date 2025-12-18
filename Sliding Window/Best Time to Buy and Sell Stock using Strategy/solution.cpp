class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<long long> prefix(n), prefix_sell(n);
        for(int i = 0; i < n; ++i) {
            if(i) {
                prefix[i] = prefix[i-1];
                prefix_sell[i] = prefix_sell[i-1];
            }
            prefix[i] += prices[i] * strategy[i];
            prefix_sell[i] += prices[i];
        }
        long long result = prefix.back();
        for(int i = 0; i + k - 1 < n; ++i) {
            int j = i + k -1;
            long long res = prefix.back() - (prefix[j] - (i ? prefix[i-1]: 0));
            res += (prefix_sell[j] - prefix_sell[j-k/2]);
            result = max(result, res);
        }
        return result;
    }
};
