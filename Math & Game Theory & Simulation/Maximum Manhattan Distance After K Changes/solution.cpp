class Solution {
public:
    int maxDistance(string s, int k) {
        unordered_map<char, int> m;
        int result{};
        auto point = [k](int a, int b) {
            int res = a;
            res += min(k, b);
            res -= max(0, b-k);
            return res;
            
        };
        for(char ch: s) {
            m[ch]++;
            int a = m['N'], b = m['S'], c = m['W'], d = m['E'];
            if(a < b) swap(a, b);
            if(c < d) swap(c, d);
            result = max(result, point(a+c,b+d));
        }
        
        return result;
    }
};
