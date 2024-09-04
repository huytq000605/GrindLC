class Solution {
    static constexpr array<pair<int, int>, 4> dirs = {{ {0, 1}, {1, 0}, {0, -1}, {-1, 0} }};
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        set<pair<int, int>> s;
        for(auto o: obstacles) {
            s.emplace(o[0], o[1]);
        }
        int i = 0, r = 0, c = 0;
        int result = 0;
        for(auto command: commands) {
            if(command == -1) {
                i = (i+1+4) % 4;
                continue;
            }
            if(command == -2) {
                i = (i-1+4) % 4;
                continue;
            }
            while(command--) {
                auto [dr, dc] = dirs[i];
                int nr = r + dr, nc = c + dc;
                if(s.find(make_pair(nr, nc)) != s.end()) {
                    break;
                }
                swap(r, nr);
                swap(c, nc);
                result = max(result, r*r + c*c);
            }
        }
        return result;
    }
};
