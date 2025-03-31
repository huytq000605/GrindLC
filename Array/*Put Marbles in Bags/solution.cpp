class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        int n = weights.size();
        if(k >= n) return 0;
        vector<long long> splits;
        for(int i = 0; i < n-1; ++i) {
            splits.emplace_back(weights[i] + weights[i+1]);
        }
        sort(splits.begin(), splits.end());
        return accumulate(splits.rbegin(), splits.rbegin()+k-1, 0ll) - accumulate(splits.begin(), splits.begin()+k-1, 0ll);
    }
};
