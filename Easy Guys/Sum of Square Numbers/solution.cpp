class Solution {
public:
    bool judgeSquareSum(int c) {
        // a**2 + b**2 = c
        long long a = 0, b = floor(sqrt(c));
        while(a <= b) {
            long long v = pow(a, 2) + pow(b, 2);
            if(v == c) {
                return true;
            } else if(v < c) {
                a++;
            } else {
                b--;
            }
        }
        return false;
    }
};
