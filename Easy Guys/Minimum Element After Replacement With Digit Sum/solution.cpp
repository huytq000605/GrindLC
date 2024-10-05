class Solution {
public:
    int minElement(vector<int>& nums) {
        vector<int> A;
        for(auto num: nums) {
            int d = 0;
            while(num) {
                d += num % 10;
                num /= 10;
            }
            A.emplace_back(d);
        }
        return *min_element(A.begin(), A.end());
    }
};
