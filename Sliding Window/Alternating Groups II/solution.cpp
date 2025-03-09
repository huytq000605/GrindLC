class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int result{};
        int n = colors.size();
        for(int i{1}, j{}; i < colors.size() + k - 1; ++i) {
            if(colors[i%n] == colors[(i-1)%n]) {
                j = i;
            }
            if(i-j+1 >= k) ++result;
        }
        return result;
    }
};
