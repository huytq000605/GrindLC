class Solution {
public:
    int maximum69Number (int num) {
        int pos = -1;
        for(int i = 0, c = num; c; i++, c /= 10) {
            if(c % 10 == 6) {
                pos = i;
            }
        }
        return num + 3 * pow(10, pos);
    }
};
