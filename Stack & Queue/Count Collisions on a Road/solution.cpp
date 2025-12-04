class Solution {
public:
    int countCollisions(string directions) {
        char last = 'L';
        int r = 0;
        int result = 0;
        for(char c: directions) {
            if(c == 'L') {
                if(last == 'S') {
                    result += 1;
                    last = 'S';
                } else if(last == 'R') {
                    result += 1 + r;
                    last = 'S';
                }
                r = 0;
            } else if(c == 'S') {
                if(last == 'R') {
                    result += r;   
                }
                last = 'S';
                r = 0;
            } else {
                ++r;
                last = 'R';
            }
        }
        return result;
    }
};
