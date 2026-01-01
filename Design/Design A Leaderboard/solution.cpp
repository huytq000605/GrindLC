class Leaderboard {
public:
unordered_map<int, int> score_map;
multiset<int> scores;
    Leaderboard() {
    }
    
    void addScore(int playerId, int score) {
        int s = score_map[playerId];
        if(s) {
            scores.erase(scores.find(s));
        }
        score_map[playerId] = s + score;
        scores.insert(s+score);
    }
    
    int top(int K) {
        int result = 0;
        int count = 0;
        for(auto it = scores.rbegin(); it != scores.rend() && count < K; ++it) {
            result += *it;
            ++count;
        }
        return result;
    }
    
    void reset(int playerId) {
        int score = score_map[playerId];
        scores.erase(scores.find(score));
        score_map.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
