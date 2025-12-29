class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int result = 0;
        int calo = 0;
        for(int i = 0; i < calories.size(); ++i) {
            if(i - k >= 0) calo -= calories[i-k];
            calo += calories[i];
            if(i >= k-1) {
                if(calo < lower) --result;
                else if(calo > upper) ++result;
            }
        }
        return result;
    }
};
