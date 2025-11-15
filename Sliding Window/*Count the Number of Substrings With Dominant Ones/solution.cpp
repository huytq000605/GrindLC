class Solution {
public:
    int numberOfSubstrings(string s) {
        int result = 0;
        for(int z = 0; z + z*z <= s.size(); z++) {
            vector<int> count(2);
            int prev_result = result;
            for(int i = 0, k = 0, j = 0; j < s.size(); ++j) {
                count[s[j]-'0']++;
                while(count[0] > z) count[s[i++]-'0']--;
                if(count[0] == z && count[1] && count[1] >= z*z) {
                    // move k to the last '1' we could start from to maintain z zeros
                    for(k = max(k, i); k < j && s[k] == '1' && count[1] >= z*z; ++k);
                    // we might move too far that we might not have enough ones
                    // check that by min with count[1] - z*z
                    result += 1 + min(k - i, count[1] - z*z);
                    
                }
                
            }
            if(result == prev_result) break;
        }
        return result;
    }
};
