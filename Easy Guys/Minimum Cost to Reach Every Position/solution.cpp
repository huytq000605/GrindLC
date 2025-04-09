class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {
        vector<int> result;
        int mn = INT_MAX;
        for(int c: cost) {
            mn = min(c, mn);
            result.emplace_back(mn);
        }
        return result;
    }
};
