class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
        auto cmp = [](vector<int>& s1, vector<int>& s2) -> bool {
            return s1[0] < s2[0] || s1[1] < s2[1];
        };
        sort(slots1.begin(), slots1.end(), cmp);
        sort(slots2.begin(), slots2.end(), cmp);
        int i = 0, j = 0;
        while(i < slots1.size() && j < slots2.size()) {
            int s1 = slots1[i][0], e1 = slots1[i][1];
            int s2 = slots2[j][0], e2 = slots2[j][1];
            if(min(e1, e2) - max(s1, s2) >= duration) return {max(s1, s2), max(s1, s2) + duration};
            if(e1 <= e2) i++;
            else j++;
        }
        return {};
    }
};
