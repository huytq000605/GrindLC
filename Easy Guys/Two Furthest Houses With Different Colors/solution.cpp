class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int i1 = -1, i2 = -1;
        int result = 0;
        for(int i = 0; i < colors.size(); ++i) {
            if(i1 == -1) {
                i1 = i;
            } else {
                if(i2 == -1 && colors[i1] != colors[i]) i2 = i;
                if(colors[i1] != colors[i]) result = i - i1;
                else if(i2 != -1 && colors[i2] != colors[i]) result = max(result, i - i2);
            }
        }
        return result;
    }
};
