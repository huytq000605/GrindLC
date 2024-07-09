class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int, int> color_to_ball;
        unordered_map<int, int> ball_to_color;
        vector<int> result;
        for(auto query: queries) {
            int ball = query[0];
            int color = query[1];
            if(ball_to_color.find(ball) == ball_to_color.end()) {
                ball_to_color[ball] = color;
                color_to_ball[color] += 1;
            } else {
                int cur_color = ball_to_color[ball];
                color_to_ball[cur_color] -= 1;
                if(color_to_ball[cur_color] == 0) color_to_ball.erase(cur_color);
                color_to_ball[color] += 1;
                ball_to_color[ball] = color;
            }
            result.emplace_back(color_to_ball.size());
        }
        return result;
    }
};
