class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        int result = 0;
        int p = 0;
        while(num1 && num2 && num3) {
            result = min(num1 % 10, min(num2 % 10, num3 % 10)) * pow(10, p++) + result;
            num1 /= 10;
            num2 /= 10;
            num3 /= 10;
        }
        return result;
    }
};
