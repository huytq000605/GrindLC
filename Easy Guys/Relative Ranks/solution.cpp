class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> athletes;
        for(int i = 0; i < score.size(); i++) {
            athletes.emplace_back(score[i], i);
        }
        sort(athletes.begin(), athletes.end(), [](auto a1, auto a2) -> bool {
            return a1.first > a2.first;
        });
        vector<string> result(score.size());
        for(int i = 0; i < athletes.size(); i++) {
            auto [_, athlete] = athletes[i];
            if(i == 0) result[athlete] = "Gold Medal";
            else if(i == 1) result[athlete] = "Silver Medal";
            else if(i == 2) result[athlete] = "Bronze Medal";
            else result[athlete] = to_string(i+1);
        }
        return result;
    }
};
