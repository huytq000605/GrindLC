class Solution {
public:
    long long numberOfSubarrays(vector<int>& nums) {
        stack<int> st;
        unordered_map<int, int> counter;
        long long result = 0;
        for(int i = 0; i < nums.size(); i++) {
            while(st.size() && nums[i] > nums[st.top()]) {
                counter[nums[st.top()]] -= 1;
                st.pop();
            }
            counter[nums[i]] += 1;
            result += counter[nums[i]];
            st.push(i);
        }
        return result;
    }
};
