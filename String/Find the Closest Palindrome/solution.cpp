class Solution {
public:
    string nearestPalindromic(string n) {
        int l = n.size();
        if(l == 1) return to_string(n[0] - '0' - 1);
        string half = n.substr(0, (l+1) / 2);
        vector<string> candidates;
        candidates.emplace_back(string(n.size() - 1, '9'));
        for(auto d: vector<int>{-1, 0, 1}) {
            long long half_int = stol(half) + d;
            string s = to_string(half_int);
            for(int i = s.size() - 1 - (l % 2); i >= 0; --i) s += s[i];
            candidates.emplace_back(s);
        }
        candidates.emplace_back('1' + string(n.size() - 1, '0') + '1');
        long long diff = INT_MAX;
        string result;
        for(auto res: candidates) {
            long long d = abs(stol(n) - stol(res));
            if(d && d < diff) {
                diff = d;
                result = res;
            }
        }
        return result;
    }
};
