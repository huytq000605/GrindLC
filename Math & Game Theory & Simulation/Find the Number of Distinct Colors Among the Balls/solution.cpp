class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        vector<int> result;
        unordered_map<int, int> color_to_num_balls;
        unordered_map<int, int> ball_to_color;
        for(auto &query: queries) {
            int ball = query[0], color = query[1];
            if(ball_to_color.find(ball) != ball_to_color.end()) {
                int old_color = ball_to_color[ball];
                color_to_num_balls[old_color] -= 1;
                if(!color_to_num_balls[old_color]) color_to_num_balls.erase(old_color);
            }
            ball_to_color[ball] = color;
            color_to_num_balls[color] += 1;
            result.emplace_back(color_to_num_balls.size());
        }
        return result;
    }
};
