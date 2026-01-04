class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int result = 0;
        for(int num: nums) {
            int s = 0;
            int ds = 0;
            for(int d = 1; d * d <= num; ++d) {
                if(num % d == 0) {
                    s +=  d;
                    s += num / d;
                    ds += d *d == num ? 1: 2;
                    if(ds > 4) {
                        break;
                    }
                }
            }
            if(ds == 4) result += s;
        }
        return result;
    }
};
