class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if(num * 9 < sum) return "";
        int n = sum / 9;
        string result(n, '9');
        sum -= n * 9;
        for(int i = n; i < num; ++i) {
            result += sum ? sum + '0' : '0';
            sum = 0;
        }
        return result;
    }
};
