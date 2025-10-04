class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0;
        for(int i = 0, j = height.size()-1; i < j;) {
            result = max(result, (j-i) * min(height[i], height[j]));
            if(height[i] <= height[j]) {
                ++i;
            } else {
                --j;
            }
        }
        return result;
    }
};
