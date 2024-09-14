class Solution {
public:
    string convertDateToBinary(string date) {
        vector<int> nums{0};
        for(char c: date) {
            if(c == '-') nums.emplace_back(0);
            else nums.back() = nums.back() * 10 + c - '0';
        }
        vector<string> ss;
        auto binary = [](int num) -> string {
            string result;
            while(num) {
                result += (num & 1) + '0';
                num >>= 1;
            }
            reverse(result.begin(), result.end());
            return result;
        };
        return format("{}-{}-{}", binary(nums[0]), binary(nums[1]), binary(nums[2]));
    }
};
