class Solution {
public:
    int smallestRepunitDivByK(int k) {
        unordered_set<int> us;
        int mod = 1 % k;
        int result = 1;
        while(mod != 0) {
            mod = (mod * 10 + 1) % k;
            if(us.find(mod) != us.end()) return -1;
            us.insert(mod);
            ++result;
        }
        return result;
    }
};
