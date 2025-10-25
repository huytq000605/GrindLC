class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7;
        int remaining = n % 7;
        int base = 1+2+3+4+5+6+7;
        // base base + 7 base + 14 
        // 0 + 7 + 14 + ... + 7*n
        int result = base * weeks + (7*(weeks-1)) * weeks / 2;
        for(int money = weeks + 1; money <= weeks + remaining; ++money) {
            result += money;
        }
        return result;
    }
};
