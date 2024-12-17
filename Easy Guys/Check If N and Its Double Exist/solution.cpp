class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> s;
        for(int num: arr) {
            if(s.find(num * 2) != s.end()) return true;
            if(!(num & 1) && s.find(num / 2) != s.end()) return true;
            s.emplace(num);
        }
        return false;
    }
};
