class Solution {
public:
    int minimumDistance(vector<vector<int>>& points) {
        // |x1 - x2| + |y1 - y2|
        // 1. (x1 - x2) + (y1 - y2) = (x1 + y1) - (x2 + y2) = sum1 - sum2
        // 2. -(x1 - x2) + (y1 - y2) = -(x1 - y1) + (x2 - y2) = diff1 - diff2
        // 3. (x1 - x2) - (y1 - y2) = (x1 - y1) - (x2 - y2) = diff1 - diff2
        // 4. -(x1 - x2) - (y1 - y2) = -(x1 + y1) + (x2 + y2) = sum1 - sum2
        // => max(|x1 - x2| + |y1 - y2|) = max(max_sum - min_sum, max_diff - min_diff)
        auto max_distance_idx = [&](int remove) {
            int min_diff = INT_MAX, max_diff = INT_MIN;
            int min_sum = INT_MAX, max_sum = INT_MIN;
            int min_diff_idx, max_diff_idx, min_sum_idx, max_sum_idx;
            for(int i = 0; i < points.size(); i++) {
                if(i == remove) continue;
                int sum = points[i][0] + points[i][1];
                int diff = points[i][0] - points[i][1];
                if(sum < min_sum) {
                    min_sum_idx = i;
                    min_sum = sum;
                }
                if(sum > max_sum) {
                    max_sum_idx = i;
                    max_sum = sum;
                }
                if(diff < min_diff) {
                    min_diff = diff;
                    min_diff_idx = i;
                }
                if(diff > max_diff) {
                    max_diff = diff;
                    max_diff_idx = i;
                }
            }
            return max(max_sum - min_sum, max_diff - min_diff) == max_sum - min_sum ?
                make_pair(max_sum_idx, min_sum_idx) :
                make_pair(max_diff_idx, min_diff_idx);
        };

        auto manhattan = [&](int i, int j) {
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
        };
        
        auto [i, j] = max_distance_idx(-1);
        auto [i1, j1] = max_distance_idx(i);
        auto [i2, j2] = max_distance_idx(j);
        return min(manhattan(i1, j1), manhattan(i2, j2));
    }
};
