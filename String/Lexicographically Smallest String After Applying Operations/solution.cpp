class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        unordered_set<string> us;
        deque<string> dq{s};
        us.insert(s);
        int n = s.size();
        string result = s;
        while(!dq.empty()) {
            auto ss = dq.front(); dq.pop_front();
            result = min(result, ss);
            auto ss1 = ss.substr(n-b) + ss.substr(0, n-b);
            if(us.find(ss1) == us.end()) {
                us.insert(ss1);
                dq.push_back(ss1);
            }
            for(int i = 1; i < ss.size(); i += 2) {
                ss[i] = (ss[i] - '0' + a) % 10 + '0';
            }
            if(us.find(ss) == us.end()) {
                us.insert(ss);
                dq.push_back(ss);
            }
        }
        return result;
    }
};
