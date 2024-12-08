class Solution {
public:
    int smallestNumber(int n) {
        int result{};
        while(result < n) {
            result <<= 1;
            result |= 1;
        }
        return result;
    }
};
