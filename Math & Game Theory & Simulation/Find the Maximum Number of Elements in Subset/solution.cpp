class Solution {
public:
    int maximumLength(vector<int>& nums) {
        unordered_map<int, int> counter;
        for(int num: nums) counter[num]++;
        int result = 1;
        for(long long num: nums) {
            if(num == 1) {
                result = max(result, counter[num] - ((counter[num]&1) == 0));
            } else {
                int cur = 0;
                while(counter[num] >= 2 && LLONG_MAX / num >= num) {
                    cur += 2;
                    num = num*num;
                }
                result = max(result, cur + (counter[num] ? 1: -1));
            }
        }
        return result;
    }
};
