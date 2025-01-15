class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int diff{};
        for(int b{}; b < 30; ++b) {
            diff += (num1 >> b) & 1;
            diff -= (num2 >> b) & 1;
        }
        int result{num1};
        if(diff > 0) {
            for(int b{}; b < 30 && diff; ++b) {
                if((result >> b) & 1) {
                    result &= ~(1 << b);
                    diff -= 1;
                }
            }
        } else if(diff < 0) {
            for(int b{}; b < 30 && diff; ++b) {
                if(((result >> b) & 1) == 0) {
                    result |= (1 << b);
                    diff += 1;
                }
            }
        }
        return result;
    }
};
