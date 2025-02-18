class Solution {
public:
    string smallestNumber(string pattern) {
        string result{};
        auto dfs = [&](this auto &dfs, int mask) {
            if(result.size() == pattern.size() + 1) return true;
            int lo{1}, hi{9};
            if(result.empty()) lo = 1;
            else if(pattern[result.size()-1] == 'I') lo = result.back()-'0'+1;
            else hi = result.back()-'0'-1;
            for(int i{lo}; i <= hi; ++i) {
                if((mask >> i) & 1) continue;
                result += i + '0';
                if(dfs(mask | (1 << i))) return true;
                result.pop_back();
            }
            return false;
        };
        dfs(0);
        return result;
    }
};
