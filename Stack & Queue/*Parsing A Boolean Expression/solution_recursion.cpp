class Solution {
public:
    bool parseBoolExpr(string expression) {
        auto parse = [&](int i, int j, auto parse_ref) -> bool {
            char op = expression[i];
            bool result{};
            int start_idx{i+2};
            int st{0};
            switch(op) {
            case 't':
                return true;
            case 'f':
                return false;
            case '!':
                return !parse_ref(i+2, j-1, parse_ref);
            case '&':
                result = true;
                for(int idx = i+1; idx <= j; ++idx) {
                    if(expression[idx] == '(') {
                        ++st;
                    } else if(expression[idx] == ')') {
                        // at the end
                        if(st == 1) result &= parse_ref(start_idx, idx-1, parse_ref);
                        --st;
                    } else if(expression[idx] == ',' && st == 1) {
                        result &= parse_ref(start_idx, idx-1, parse_ref);
                        start_idx = idx+1;
                    }
                }
                return result;
            case '|':
                result = false;
                for(int idx = i+1; idx <= j; ++idx) {
                    if(expression[idx] == '(') {
                        ++st;
                    } else if(expression[idx] == ')') {
                        // at the end
                        if(st == 1) result |= parse_ref(start_idx, idx-1, parse_ref);
                        --st;
                    } else if(expression[idx] == ',' && st == 1) {
                        result |= parse_ref(start_idx, idx-1, parse_ref);
                        start_idx = idx+1;
                    }
                }
                return result;
            }
            return false;
        };
        return parse(0, expression.size() - 1, parse);
    }
};
