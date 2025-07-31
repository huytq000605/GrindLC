class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> s;
        unordered_set<int> result;
        for(int num: arr) {
            unordered_set<int> ns{num};
            result.insert(num);
            for(auto v: s) {
                ns.insert(v | num);
                result.insert(v | num);
            }
            s = move(ns);
        }
        return result.size();
    }
};
