class Solution:
    def evaluate(self, expression: str) -> int:
        values = dict()

        def cal(start_exp):
            nonlocal values
            
            # We process each layer
            if start_exp[0] == "(":
                return cal(start_exp[1:-1])
            
            # Get each expression into exps array
            exps = [""]
            stack = 0
            for l in start_exp:
                if l == " " and stack == 0:
                    exps.append("")
                    continue
                elif l == "(":
                    stack += 1
                elif l == ")":
                    stack -= 1    
                exps[-1] += l
                
            # Process this layer
            n = len(exps)
            if exps[0] == "let":
                old_values = dict()
                for i in range(1, n-1, 2):
                    # We store old value to use in the outer scope
                    key = exps[i]
                    if key in values:
                        old_values[key]  = values[key]
                    values[key] = cal(exps[i+1])
                result = cal(exps[-1])
                # We dfs all values inside, revert old value back to outser scope
                for key, value in old_values.items():
                    values[key] = value
                return result
            elif exps[0] == "add":
                return cal(exps[1]) + cal(exps[2])
            elif exps[0] == "mult":
                return cal(exps[1]) * cal(exps[2])
            else:
                if exps[0] in values: return values[exps[0]]
                else: return int(exps[0])
            
        result = cal(expression)
        return result