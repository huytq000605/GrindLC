class Solution {
public:
    bool judgeCircle(string moves) {
        int r = 0, u = 0;
        for(auto c: moves) {
            if(c == 'U') ++u;
            else if(c == 'D') --u;
            else if(c == 'R') ++r;
            else --r;
        }
        return !r && !u;
    }
};
