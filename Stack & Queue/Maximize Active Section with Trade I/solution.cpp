class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        deque<pair<char, int>> dq;
        dq.emplace_back(s[0], 1);
        int active = s[0] == '1';
        int bonus = 0;
        for(int i = 1; i < s.size(); ++i) {
            if(s[i] == s[i-1]) {
                dq.back().second += 1;
            } else {
                dq.emplace_back(s[i], 1);
            }
            while(dq.size() > 3 || dq.front().first == '1') {
                dq.pop_front();
            }
            if(dq.size() == 3) {
                bonus = max(bonus, dq.front().second + dq.back().second);
            }
            active += s[i] == '1';
        }
        return active + bonus;
    }
};
