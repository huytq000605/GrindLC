class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int f = 0, t = 0;
        for(int b: bills) {
            int change = b - 5;
            if(change) {
                if(change >= 10 && t) {
                    t -= 1;
                    change -= 10;
                }
                if(change / 5 > f) return false;
                f -= change / 5;
            }
            if(b == 5) f += 1;
            else if(b == 10) t += 1;
        }
        return true;
    }
};
