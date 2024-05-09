class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        priority_queue<int> pq(happiness.begin(), happiness.end(), less<int>());
        int turn = 0;
        long long result = 0;
        while(k && pq.top() - turn > 0) {
            result += max(0, pq.top() - turn++);
            pq.pop();
            k--;
        }
        return result;
    }
};
