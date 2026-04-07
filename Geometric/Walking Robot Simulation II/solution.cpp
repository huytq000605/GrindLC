class Robot {
static constexpr array<tuple<string, int, int>, 4> ds {{{"East", 0, 1}, {"North", 1, 0}, {"West", 0, -1}, {"South", -1, 0}}};
int m, n, di = 0, r = 0, c = 0;
public:
    Robot(int width, int height) {
        n = width;
        m = height;
    }
    
    void step(int num) {
        num %= ((m+n)*2-4);
        // trap, if it finished the whole lap, the direction changes
        if(num == 0) num = (m+n)*2-4;
        while(num) {
            auto [_, dr, dc] = ds[di];
            if(r + dr < 0 || r + dr >= m || c + dc < 0 || c + dc >= n) {
                di = (di + 1) % 4;
                continue;
            }
            r += dr;
            c += dc;
            --num;
        }
    }
    
    vector<int> getPos() {
        return {c, r};
    }
    
    string getDir() {
        return get<0>(ds[di]);
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
