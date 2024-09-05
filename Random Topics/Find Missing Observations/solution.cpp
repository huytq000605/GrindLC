class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int s = mean * (m + n);
        int m_rolls = accumulate(rolls.begin(), rolls.end(), 0);
        int n_rolls = s - m_rolls;
        if(n > n_rolls || 6 * n < n_rolls) return {};
        int each = n_rolls / n;
        int mod = n_rolls % n;
        vector<int> result(n, each);
        for(int i = 0; i < mod; i++) result[i]++;
        return result;
    }
};
