class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int volume, int k) {
        while(volume--) {
            int u = -1;
            int v = INT_MAX;
            for(int i = k-1; i >= 0; --i) {
                if(heights[i] > heights[i+1]) break;
                else if(heights[i] < heights[i+1] && heights[i] < v) {
                    v = heights[i];
                    u = i;
                }
            }
            if(u != -1) {
                heights[u]++;
                continue;
            }
            
            u = -1;
            v = INT_MAX;
            for(int i = k+1; i < heights.size(); ++i) {
                if(heights[i] > heights[i-1]) break;
                else if(heights[i] < heights[i-1] && heights[i] < v) {
                    v = heights[i];
                    u = i;
                }
            }
            if(u != -1) {
                heights[u]++;
            } else {
                heights[k]++;
            }
        }
        return heights;
    }
};
