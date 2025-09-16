class Solution {
public:
    int gcd(int a, int b) {
        if(a < b) swap(a, b);
        if(b == 0) return a;
        return gcd(b, a % b);
    }
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> result;
        for(int i = 0; i < nums.size(); ++i) {
            result.push_back(nums[i]);
            while(result.size() >= 2) {
                int a = result.back();
                int b = result[result.size() - 2];
                int gcd_ab = gcd(a, b);
                if(gcd_ab == 1) break;
                result.pop_back();
                result.pop_back();
                result.push_back(1LL * a * b / gcd_ab); 
            }
        }
        return result;
    }
};
