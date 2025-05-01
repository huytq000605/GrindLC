class SnakeGame {
int m, n;
deque<pair<int, int>> dq;
vector<vector<int>> food, count;
int ifood = 0;
public:
    SnakeGame(int width, int height, vector<vector<int>>& _food) {
        m = height;
        n = width;
        food = _food;
        count.resize(m);
        for(int i = 0; i < m; ++i) count[i].resize(n);
        dq.emplace_back(0, 0);
    }
    
    int move(string direction) {
        pair<int, int> d;
        if(direction == "U")
            d = {-1, 0};
        else if(direction == "R")
            d = {0, 1};
        else if(direction == "D")
            d = {1, 0};
        else
            d = {0, -1};
        auto [dr, dc] = d;
        auto [r, c] = dq.back();
        auto [tr, tc] = dq.front(); dq.pop_front();
        count[tr][tc]--;
        int nr = r + dr, nc = c + dc;
        if(!valid(nr, nc)) return -1;
        count[nr][nc]++;
        dq.emplace_back(nr, nc);
        if(ifood < food.size() && food[ifood][0] == nr && food[ifood][1] == nc) {
            ifood++;
            dq.emplace_front(tr, tc);
            count[tr][tc]++;
        }
        if(count[nr][nc] > 1) return -1;
        return dq.size() - 1;
    }

    bool valid(int r, int c) {
        return r >= 0 && r < m && c >= 0 && c < n;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame* obj = new SnakeGame(width, height, food);
 * int param_1 = obj->move(direction);
 */
