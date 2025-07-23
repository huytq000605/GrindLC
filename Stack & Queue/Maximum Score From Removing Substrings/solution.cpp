class Solution {
public:
    int maximumGain(string s, int x, int y) {
        string u = "ab", v = "ba";
        if(x < y) {
            swap(u, v);
            swap(x, y);
        }
        auto cal = [](string& s, string& p, int v) -> int {
            int j = 0, result = 0;
            for(int i = 0; i < s.size(); ++i) {
                s[j++] = s[i];
                if(j > 1 && s[j-1] == p[1] && s[j-2] == p[0]) {
                    j -= 2;
                    result += v;
                }
            }
            s.resize(j);
            return result;
        };
        return cal(s, u, x) + cal(s, v, y);
    }
};
