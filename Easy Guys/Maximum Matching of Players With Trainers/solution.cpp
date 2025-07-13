class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());
        int t = 0;
        int result = 0;
        for(auto &player: players) {
            while(t < trainers.size() && trainers[t] < player) {
                ++t;
            }
            if(t == trainers.size()) break;
            ++result;
            ++t;
        }
        return result;
    }
};
