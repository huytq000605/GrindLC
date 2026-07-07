class Solution {
public:
    long long sumAndMultiply(int n) {
        int s = 0;
        long long result = 0;
        for(int mul = 1; n; n /= 10) {
            if(n % 10) {
                s += n % 10;
                result += (n % 10) * mul;
                mul *= 10;
            }
        }
        return result * s;
    }
};
