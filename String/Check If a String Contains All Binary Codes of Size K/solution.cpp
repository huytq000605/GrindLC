class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<int> covered;
        int all_set = (1 << k) - 1;
        for(int i = 0, mask = 0; i < s.size(); ++i) {
            mask = (mask << 1) | (s[i] - '0');
            mask &= all_set;
            if(i >= k - 1) {
                covered.emplace(mask);
                if(covered.size() == (1 << k)) return true;
            }
        }
        return false;
    }
};
