class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        map<int, int> values;
        for(int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if(num == 0) values[0] = mapping[0];
            else {
                int jumbled_num = 0;
                int mul = 1;
                while(num) {
                    jumbled_num += mapping[num % 10] * mul;
                    num /= 10;
                    mul *= 10;
                }
                values[nums[i]] = jumbled_num;
            }            
        }
        sort(nums.begin(), nums.end(), [&](auto a, auto b) {
            return values[a] < values[b];
        });
        return nums;
    }
};
