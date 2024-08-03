class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        map<int, int> counter;
        for(auto c: target) counter[c] += 1;
        for(auto c: arr) {
            if(!counter[c]) return false;
            counter[c] -= 1;
        }
        return true;
    }
};
