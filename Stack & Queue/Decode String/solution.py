class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        curNum = 0
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = ""
            elif s[i] == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
                curNum = 0
            elif s[i].isnumeric():
                curNum = curNum * 10 + int(s[i])
            else:
                curString += s[i]
        return curString