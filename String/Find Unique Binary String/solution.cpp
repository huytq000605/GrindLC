class Solution {
private:
    string to_binary(int num, int width) {
        string s;
        while (num) {
            s += to_string(num & 1);
            num >>= 1;
        }
        while(s.size() < width) s += "0";
        return {s.rbegin(), s.rend()};
    }
public:
    string findDifferentBinaryString(vector<string>& snums) {
        int n = snums.size();
        vector<int> nums(1<<n);
        for(string &snum: snums) {
            int num{};
            for(int i = snum.size() - 1, v = 1; i >= 0; --i, v *= 2) {
                num += v * (snum[i] - '0');
            }
            nums[num] = 1;
        }
        for(int i{}; i < 1<<n; ++i) if(!nums[i]) return to_binary(i, n);
        return "";
    }
};
