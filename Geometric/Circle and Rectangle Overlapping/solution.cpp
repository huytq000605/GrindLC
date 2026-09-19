class Solution {
public:
    bool checkOverlap(int radius, int x, int y, int x1, int y1, int x2, int y2) {
        // px, py is the point that in rectangle closest to the center of circle
        int px = x, py = y;
        if(px < x1) px = x1;
        else if(px > x2) px = x2;
        if(py < y1) py = y1;
        else if(py > y2) py = y2;
        return (px-x)*(px-x) + (y-py)*(y-py) <= radius*radius;
    }
};
