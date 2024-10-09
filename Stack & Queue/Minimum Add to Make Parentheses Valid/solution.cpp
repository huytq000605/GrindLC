class Solution {
public:
    int minAddToMakeValid(string s) {
        int st = 0;
        int result = 0;
        for(auto c: s) {
            if(c == '(') ++st;
            else --st;
            if(st < 0) {
                st = 0;
                ++ result;
            }
        }
        return result + st;
    }
};
