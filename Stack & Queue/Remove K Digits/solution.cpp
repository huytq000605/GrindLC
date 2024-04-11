class Solution {
public:
    string removeKdigits(string num, int k) {
        string result;
        for(auto & c: num) {
            while(k && result.size() && result.back() > c) {
                result.pop_back();
                k -= 1;
            }
            if(c == '0' && !result.size()) continue;
            result.push_back(c);
        };
        while(k && result.size()) {
            result.pop_back();
            k--;
        }
        if(!result.size()) return "0";
        return result;
    }
};
