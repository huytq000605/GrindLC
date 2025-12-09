class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map<int, unordered_map<int, int>> t, v;

        for (int i = 0; i < points.size(); ++i) {
            for (int j = i + 1; j < points.size(); ++j) {

                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx < 0 || (dx == 0 && dy < 0))
                    dx = -dx, dy = -dy;

                int g = std::gcd(dx, std::abs(dy));

                int sx = dx / g;
                int sy = dy / g;

                int des = sx * points[i][1] - sy * points[i][0];

                int key1 = (sx << 12) | (sy + 2000);
                int key2 = (dx << 12) | (dy + 2000);

                ++t[key1][des];
                ++v[key2][des];
            }
        }
        /*
        Points on the same line:
        A --- B --- C --- D
        Segments on this line:
        AB
        AC
        AD
        BC
        BD
        CD

        Any pair among them is invalid for forming trapezoids, but v will count:

        AB vs BC
        BC vs AB
        AB vs CD
        CD vs AB
        ...

        Everything twice.
        Hence the /2.
        */
        return count(t) - count(v) / 2;
    }

    int count(unordered_map<int, unordered_map<int, int>>& mp) {
        long long ans = 0;

        for (auto& [k1, inner] : mp) {
            long long sum = 0;
            for (auto& [k2, val] : inner)
                sum += val;

            for (auto& [k2, val] : inner)
                ans += val * (sum -= val);
        }

        return ans;
    }
};
