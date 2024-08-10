class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        vector<vector<int>> players(n, vector<int>(11, 0));
        set<int> wins;
        for(auto p: pick) {
            players[p[0]][p[1]] += 1;
            if(players[p[0]][p[1]] > p[0]) wins.emplace(p[0]);
        }
        return wins.size();
    }
};
