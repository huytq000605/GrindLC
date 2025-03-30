class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> last(26, -1);
        for(int i = 0; i < s.size(); ++i) {
            last[s[i] - 'a'] = i;
        }
        vector<int> result;
        for(int i = 0, j = -1, start = 0; i < s.size(); ++i) {
            j = max(j, last[s[i] - 'a']);
            if(i == j) {
                result.emplace_back(i - start + 1);
                j = -1;
                start = i+1;
            }
        }
        return result;
    }
};
