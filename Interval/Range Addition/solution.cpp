class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> result(length);
        for(auto &update: updates) {
            int s = update[0], e = update[1], i = update[2];
            result[s] += i;
            if(e+1 < length) result[e+1] -= i;
        }
        for(int i = 0, pref = 0; i < length; ++i) {
            pref += result[i];
            result[i] = pref;
        }
        return result;
    }
};
