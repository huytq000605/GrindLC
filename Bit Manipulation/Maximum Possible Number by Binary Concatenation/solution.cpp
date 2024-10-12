class Solution {
public:
    int maxGoodNumber(vector<int>& nums) {
        auto to_binary = [](int num) -> string {
            string result;
            while(num) {
                result += to_string(num & 1);
                num >>= 1;
            }
            return string(result.rbegin(), result.rend());
        };
        vector<string> binaries;
        for(int num: nums) binaries.emplace_back(to_binary(num));
        sort(binaries.begin(), binaries.end(), [](auto &b1, auto &b2) -> bool {
            return b1 + b2 > b2 + b1;
        });
        string s;
        for(auto &b: binaries) s += b;
        int result = 0;
        for(int i = 0; i < s.size(); ++i) {
            result += pow(2, i) * (s[s.size()-1-i] - '0');
        }
        return result;
    }
};
