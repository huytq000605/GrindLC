class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int r = 0, c = 0;
        for(auto command: commands) {
            if(command == "UP") r--;
            else if(command == "LEFT") c--;
            else if(command == "RIGHT") c++;
            else r++;
        }
        return r * n + c;
    }
};
