class Solution {
public:
    int getLucky(string s, int k) {
        string ds;
        for(auto c: s) ds += to_string(c - 'a' + 1);
        int num = 0;
        while(k--) {
            num = 0;
            for(auto c: ds) num += c - '0';
            ds = to_string(num);
        }
        return num;
    }
};
