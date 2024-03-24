class Solution {
public:
    bool checkArray(vector<int>& nums, int k) {
        std::deque<std::pair<int, int>> dq;
        int s = 0;
        for(int i = 0; i < nums.size(); i++) {
            while(dq.size() > 0 && i - dq[0].first + 1 > k) {
                s -= dq.front().second;
                dq.pop_front();
            }
            if(nums[i] - s < 0) return false;
            if(nums[i] - s) {
                if(i + k - 1 >= nums.size()) return false;
                dq.push_back(std::make_pair(i, nums[i] - s));
                s = nums[i];
            }
        }
        return true;
    }
};
