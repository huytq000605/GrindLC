class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int &a, int &b) -> bool {
            string s1 = to_string(a), s2 = to_string(b);
            return s1 + s2 > s2 + s1;
        });
        string result;
        for(auto num: nums) {
            result += to_string(num);
        }
        if(result[0] == '0') return "0";
        return result;
    }
};
