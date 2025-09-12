class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size(), m = mana.size();
        vector<long long> t(n);
        for(int potion = 0; potion < m; ++potion) {
            for(int p = n-2; p >= 0; --p) {
                t[p] = max(t[p], t[p+1] - skill[p] * mana[potion]);
            }
            for(int p = 0; p < n; ++p) {
                t[p] = max(p ? t[p-1]: 0, t[p]) + skill[p] * mana[potion];
            }
        }
        return t.back();
    }
};
