impl Solution {
    pub fn parse_ternary(expression: String) -> String {
        let mut stack = vec![];
        let mut idx = expression.len() - 1;
        let exp = expression.as_bytes();
        while true {
            if exp[idx] != '?' as u8 && exp[idx] != ':' as u8 {
                stack.push(exp[idx]);
            } else if exp[idx] == '?' as u8 {
                idx -= 1;
                let (first, second) = (stack.pop().unwrap(), stack.pop().unwrap());
                if exp[idx] == 'T' as u8 {
                    stack.push(first);
                } else {
                    stack.push(second);
                }
            }
            if idx == 0 {
                break
            }
            idx -= 1;
        }
        return (stack[0] as char).to_string()
    }
}
