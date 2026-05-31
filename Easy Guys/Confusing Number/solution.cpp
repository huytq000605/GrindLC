class Solution {
public:
    bool confusingNumber(int n) {
        int a = n, b = 0;
        while(n) {
            int d = n % 10;
            if(d == 2 || d == 3 || d == 4 || d == 5 || d == 7) return false;
            n /= 10;
            b = b * 10 + (d == 6 ? 9: d == 9 ? 6: d);
        }
        return a != b;
    }
};
