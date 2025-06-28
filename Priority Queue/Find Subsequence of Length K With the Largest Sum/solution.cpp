class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        priority_queue<int> pq;
        for(auto num: nums) {
            pq.emplace(-num);
            if(pq.size() > k) pq.pop();
        }
        while(!pq.empty()) {
            counter[pq.top()]++;
            pq.pop();
        }
        vector<int> result;
        for(int num: nums) {
            num = -num;
            if(counter.find(num) != counter.end()) {
                result.emplace_back(-num);
                counter[num]--;
                if(!counter[num]) counter.erase(num);
            }
        }
        return result;
    }
};
