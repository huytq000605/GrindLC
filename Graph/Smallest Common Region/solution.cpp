class Solution {
public:
    string findSmallestRegion(vector<vector<string>>& regions, string region1, string region2) {
        map<string, string> parents;
        for(auto &r: regions) {
            string &r0 = r[0];
            for(int i = 1; i < r.size(); ++i) {
                parents[r[i]] = r[0];
            }
        }
        set<string> ancestors1;
        ancestors1.emplace(region1);
        while(parents.find(region1) != parents.end()) {
            region1 = parents[region1];
            ancestors1.emplace(region1);
        }
        while(region2 != region1 && ancestors1.find(region2) == ancestors1.end()) {
            region2 = parents[region2];
        }
        return region2;
    }
};
