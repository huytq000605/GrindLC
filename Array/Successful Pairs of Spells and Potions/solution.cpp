class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<pair<int, int>> ispells(spells.size()), ipotions(potions.size());
        for(int i = 0; i < spells.size(); ++i) {
            ispells[i] = {i, spells[i]};
        }
        auto cmp = [](auto &p1, auto &p2) -> bool {
            return p1.second < p2.second;
        };
        sort(potions.begin(), potions.end());
        sort(ispells.begin(), ispells.end(), cmp);
        vector<int> result(spells.size());
        for(int i = 0, j = potions.size() - 1; i < spells.size(); ++i) {
            while(j >= 0 && 1LL * ispells[i].second * potions[j] >= success) --j;
            result[ispells[i].first] = (potions.size() - 1 - j);
        }
        return result;
    }
};
