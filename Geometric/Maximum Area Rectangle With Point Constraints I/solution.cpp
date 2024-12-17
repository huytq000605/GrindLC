class Solution {
public:
    int maxRectangleArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        int n = points.size();
        int result{-1};
        for(int mask{}; mask < 1 << n; ++mask) {
            vector<pair<int, int>> vertices;
            for(int bit{}; bit < n; ++bit) {
                if((mask >> bit) & 1) vertices.emplace_back(points[bit][0], points[bit][1]);
            }
            if(vertices.size() != 4) continue;
            
            // Check if its a rectangle
            pair<int, int> bl = vertices[0], tl = vertices[1], br = vertices[2], tr = vertices[3];
            if(bl.second != br.second || bl.first != tl.first || tl.second != tr.second) continue;
            bool inside_point{false};
            for(int bit{}; bit < n; ++ bit) {
                if(((mask >> bit) & 1) == 0) {
                    int x{points[bit][0]}, y{points[bit][1]};
                    if(x >= bl.first && x <= tr.first && y >= bl.second && y <= tr.second) {
                        inside_point = true;
                        break;
                    }
                }
            }
            if(inside_point) continue;
            result = max(result, (br.first - bl.first) * (tl.second - bl.second));
        }
        return result;
    }
};
