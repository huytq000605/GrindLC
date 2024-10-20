class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<pair<char, bool>> st{};
        st.emplace('&', true);
        for(int i = 0; i < expression.size(); ++i) {
            char c = expression[i];
            if(c == '(') {
                char op = expression[i-1];
                st.emplace(op, op == '&');
            } else if(c == ')') {
                auto [_, vin] = st.top();
                st.pop();
                auto &[op, vout] = st.top();
                if(op == '&') vout &= vin;
                else if(op == '|') vout |= vin;
                else if (op == '!') vout = !vin;
            } else if(c == 'f' || c == 't') {
                auto &[op, v] = st.top();
                if(op == '&') v &= (c == 't'? true : false);
                else if(op == '|') v |= (c == 't' ? true: false);
                else if(op == '!') v = !(c == 't' ? true: false);
            }
        }
        return st.top().second;
    }
};
