class Solution {
public:
    string countOfAtoms(string formula) {
        vector<map<string, int>> s{{}};
        int i = 0, n = formula.size();
        string prev = "";
        while(i < n) {
            char c = formula[i];
            if(c == '(') {
                s.emplace_back(map<string, int>());
                i++;
            } else if(c == ')') {
                i++;
                int count = 0;
                while(i < n && isdigit(formula[i])) {
                    count = count * 10 + (formula[i++] - '0');
                }
                if(!count) count = 1;
                auto elements = s.back();
                s.pop_back();
                for(auto element: elements) {
                    s.back()[element.first] += element.second * count;
                }
            } else if(isalpha(formula[i])) {
                string element = string(1, formula[i++]);
                while(i < n && islower(formula[i])) {
                    element += formula[i];
                    i++;
                }
                s.back()[element] += 1;
                prev = element;
            } else if(isdigit(formula[i])) {
                int count = 0;
                while(i < n && isdigit(formula[i])) {
                    count = count * 10 + (formula[i++] - '0');
                }
                s.back()[prev] += count - 1;
            }
        }
        string result;
        for(auto e: s.back()) {
            result += e.first + (e.second > 1 ? to_string(e.second) : "");
        }
        return result;
    }
};
