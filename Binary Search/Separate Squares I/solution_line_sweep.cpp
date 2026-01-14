class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        vector<pair<long long, long long>> sqs;
        long long total_area = 0;
        for(auto &sq: squares) {
            long long x = sq[0], y = sq[1], l = sq[2];
            sqs.emplace_back(y, l);
            sqs.emplace_back(y+l, -l);
            total_area += l*l;
        }
        sort(sqs.begin(), sqs.end(), [](auto &s1, auto &s2) -> bool {
            return s1.first < s2.first;
        });
        long long area = 0;
        long long width = 0;
        long long prev_y = sqs[0].first;
        for(auto [y, l]: sqs) {
            long long darea = width * (y - prev_y);
            if((area + darea)*2 >= total_area) {
                return (total_area/2.0 - area) / double(width) + prev_y;
            }
            width += l;
            area += darea;
            prev_y = y;
        }
        return -1;
    }
};
