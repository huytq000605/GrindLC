class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int result = INT_MAX;
        for(int i = 0; i < words.size(); ++i) {
            if(words[i] == target) {
                int d = abs(startIndex - i);
                result = min(result, min(d, int(words.size()) -  d));
            }
        }
        if(result == INT_MAX) return -1;
        return result;
    }
};
