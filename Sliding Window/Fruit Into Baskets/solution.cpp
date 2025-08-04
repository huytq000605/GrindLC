class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> m;
        int result = 0;
        int j = 0;
        for(int i = 0; i < fruits.size(); ++i) {
            if(m.find(fruits[i]) == m.end()) {
                while(m.size() == 2) {
                    m[fruits[j]] -= 1;
                    if(!m[fruits[j]]) m.erase(fruits[j]);
                    ++j;
                }
            }
            m[fruits[i]] += 1;
            result = max(result, i - j + 1);
        }
        return result;
    }
};
