class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        auto bfs = [](auto& initialCurrency, auto initivalValue, auto& pairs, auto& rates) {
            unordered_map<string, vector<pair<string, double>>> conv;
            for(int i{}; i < pairs.size(); ++i) {
                string u = pairs[i][0], v = pairs[i][1];
                double r = rates[i];
                conv[u].emplace_back(v, r);
                conv[v].emplace_back(u, 1/r);
            }
            unordered_map<string, double> currencies;
            currencies[initialCurrency] = initivalValue;
            deque<pair<string, double>> dq;
            dq.emplace_back(initialCurrency, initivalValue);
            while(!dq.empty()) {
                auto [u, val] = dq.front(); dq.pop_front();
                for(auto [v, r]: conv[u]) {
                    if(currencies.find(v) != currencies.end()) continue;
                    currencies[v] = val * r;
                    dq.emplace_back(v, val * r);
                }
            }
            return currencies;
        };
        auto after_day1 = bfs(initialCurrency, 1.0, pairs1, rates1);
        double result{};
        for(auto [currency, value]: after_day1) {
            auto after_day2 = bfs(currency, value, pairs2, rates2);
            result = max(result, after_day2[initialCurrency]);
        }
        
        return result;
    }
};
