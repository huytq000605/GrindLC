class Solution {
int MOD = pow(10, 9) + 7;
public:
    int numOfSubarrays(vector<int>& arr) {
        array<int, 2> parity;
        parity[0] = 1;
        int result{};
        for(int i{}, s{}; i < arr.size(); ++i) {
            s = (s + arr[i]) & 1;
            parity[s&1]++;
            result = (result + parity[1^(s&1)]) % MOD;
        }
        return result;
    }
};
