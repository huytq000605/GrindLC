class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        int s = std::accumulate(possible.begin(), possible.end(), 0);
        int n = possible.size();
        int points = 0;
        int opp = s + (n-s) * -1;
        for(int i = 0; i < n-1; i++) {
            if(possible[i]) {
                points += 1;
                opp -= 1;
            } else {
                points -= 1;
                opp += 1;
            }
            if(points > opp) return i+1;
        }
        return -1;
    }
};
