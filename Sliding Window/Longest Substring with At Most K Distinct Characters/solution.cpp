class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int start = 0, result = 0;
        unordered_map<char, int> counter;
        for(int i = 0; i < s.size(); i++) {
            counter[s[i]] += 1;
            while(counter.size() > k) {
                if(counter[s[start]] == 1) counter.erase(s[start]);
                else counter[s[start]] -= 1;
                start += 1;
            }
            result = max(result, i - start + 1);
        }
        return result;
    }
};
