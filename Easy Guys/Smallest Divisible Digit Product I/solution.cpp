class Solution {
public:
    int smallestNumber(int n, int t) {
        while(1) {
            int num = n;
            int product = 1;
            while(num) {
                product *= num % 10;
                num /= 10;
            }
            if(product % t == 0) return n;
            ++n;
        }
        return -1;
    }
};
