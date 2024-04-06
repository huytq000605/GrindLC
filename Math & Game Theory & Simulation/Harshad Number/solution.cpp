class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int s = 0;
        int n = x;
        while(x) {
            s += x % 10;
            x /= 10;
        }
        if(n % s == 0) {
            return s;
        }
        return -1;
    }
};
