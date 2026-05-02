class Solution {
    bool is_valid(int num) {
        bool changed = false;
        while(num) {
            int d = num % 10;
            if(d == 3 || d == 4 || d == 7) return false;
            changed |= (d == 6 || d == 9 || d == 2 || d == 5);
            num /= 10;
        }
        return changed;
    }
public:
    int rotatedDigits(int n) {
        int result = 0;
        for(int num = 1; num <= n; ++num) {
            if(is_valid(num)) result++;
        }
        return result;
    }
};
