class Solution {
public:
    string losingPlayer(int x, int y) {
        vector<string> players{"Alice", "Bob"};
        int i = 0;
        while(1) {
            if(x < 1 || y < 4) return players[1-i];
            x -= 1;
            y -= 4;
            i = 1-i;
        }
        return "";
    }
};
