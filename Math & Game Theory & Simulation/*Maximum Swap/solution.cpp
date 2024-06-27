class Solution {
public:
    int maximumSwap(int num) {
        int high_digit = 0, high_pos = 0;
        int low_digit = 0, low_pos = 0;
        int greatest_digit = 0, greatest_pos = 0;
        int pos = 1;
        int result = num;
        // Loop digit from right to left
        // Storing the right most greatest digit
        // and swap with the digit on the left whenever has a chance
        while(num) {
            int digit = num % 10;
            num /= 10;
            if(digit > greatest_digit) {
                greatest_digit = digit;
                greatest_pos = pos;
            } else if(digit < greatest_digit) {
                high_digit = greatest_digit;
                high_pos = greatest_pos;
                low_digit = digit;
                low_pos = pos;
            }
            pos *= 10;
        }
        return result + high_digit * (low_pos - high_pos) + low_digit * (high_pos - low_pos);
    }
};
