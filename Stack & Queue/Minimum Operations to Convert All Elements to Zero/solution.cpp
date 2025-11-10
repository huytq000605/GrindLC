class Solution {
public:
    int minOperations(vector<int>& nums) {
        vector<int> st;
        int result = 0;
        for(int num: nums) {
            while(!st.empty() && st.back() > num) {
                result += 1;
                st.pop_back();
            }
            if(num == 0 || (!st.empty() && num == st.back())) continue;
            st.push_back(num);
        }
        return result + st.size();
    }
};
