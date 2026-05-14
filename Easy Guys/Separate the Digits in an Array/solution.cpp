class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> result;
        for(int num: nums) {
            vector<int> digits;
            while(num) {
                digits.push_back(num % 10);
                num /= 10;
            }
            reverse(begin(digits), end(digits));
            for(int d: digits) result.push_back(d);
        }
        return result;
    }
};
