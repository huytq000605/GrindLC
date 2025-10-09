class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size(), m = mana.size();
        vector<long long> t(n);
        for(int p = 0; p < m; ++p) {
            for(int w = n-2; w >= 0; --w) {
                t[w] = max(t[w], t[w+1] - skill[w] * mana[p]);
            }
            for(int w = 0; w < n; ++w) {
                t[w] = max(w ? t[w-1]: 0, t[w]) + skill[w] * mana[p];
            }
        }
        return t.back();
    }
};
