class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& boxes) {
        int n = status.size();
        vector<int> can_open;
        unordered_set<int> opened, own;
        for(int box: boxes) {
            if(status[box]) can_open.emplace_back(box);
            else own.emplace(box);
        }
        int result = 0;
        while(!can_open.empty()) {
            int box = can_open.back(); can_open.pop_back();
            result += candies[box];
            for(auto &nbox: containedBoxes[box]) {
                if(opened.find(nbox) != opened.end()) continue;
                if(status[nbox]) can_open.emplace_back(nbox);
                else own.emplace(nbox);
            }
            for(auto& nbox: keys[box]) {
                status[nbox] = 1;
                if(own.find(nbox) != own.end()) {
                    own.erase(nbox);
                    can_open.emplace_back(nbox);
                }
            }
        }
        return result;
    }
};
