class Solution {
public:
    string getHappyString(int n, int k) {
        int options = 1 << (n-1);
        if(3 * options < k) return "";
        string result;
        for(int i = 0; i < n; ++i) {
            for(char c = 'a'; c <= 'c'; ++c) {
                if(!result.empty() && result.back() == c) continue;
                if(k - options <= 0) {
                    result += c;
                    break;
                }
                k -= options;
            }
            options >>= 1;
        }
        return result;
    }
};
