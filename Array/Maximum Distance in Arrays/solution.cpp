class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int mn = arrays[0].front(), mx = arrays[0].back();
        int result = 0;
        for(int i = 1; i < arrays.size(); i++) {
            result = max(result, arrays[i].back() - mn);
            result = max(result, mx - arrays[i].front());
            mn = min(mn, arrays[i].front());
            mx = max(mx, arrays[i].back());
        }
        return result;
    }
};
