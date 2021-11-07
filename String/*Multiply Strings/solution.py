class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                n1 = int(num1[i])
                n2 = int(num2[j])
                idx = i + j
                product = n1 * n2 + result[idx + 1]
                result[idx + 1] = product % 10
                result[idx] += product // 10
        
        MSB = 0
        while(result[MSB] == 0):
            MSB += 1
        return "".join([str(value) for value in result[MSB:]])