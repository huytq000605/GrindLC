class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.rbegin(), happiness.rend());
        long long result = 0;
        for(int i = 0, selected = 0; i < happiness.size() && happiness[i] - selected >= 0 && selected < k; ++i) {
            result += happiness[i] - selected++;
        }
        return result;
    }
};
