class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int total_shift{};
        for(auto &sh: shift) {
            int d{sh[0]}, a{sh[1]};
            total_shift += d == 0 ? -a: a;
        }
        int n = s.size();
        total_shift = (total_shift % n + n) % n;
        if(!total_shift) return s;
        return s.substr(s.size() - total_shift) + s.substr(0, s.size() - total_shift);
    }
};
