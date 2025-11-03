class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int result = 0;
        for(int i = 0; i < colors.size(); ++i) {
            int mx = neededTime[i];
            int cost = 0;
            char c = colors[i];
            while(i+1 < colors.size() && colors[i+1] == c) {
                if(!cost) cost += neededTime[i];
                ++i;
                mx = max(mx, neededTime[i]);
                cost += neededTime[i];
            }
            if(cost) {
                result += cost - mx;
            }
        }
        return result;
    }
};
