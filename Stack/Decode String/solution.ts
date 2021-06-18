function decodeString(s: string): string {
    let stack = []
    let result = s
    for(let i = 0; i < result.length; i++) {
        if(result[i] == "[") {
            stack.push(i)
            continue;
        }
        if(result[i] == "]") {
            let start = stack.pop()
            let [num, numLength] = getNumber(result, start)
            let str = result.slice(start + 1, i)
            let finalStr = str
            for(let i = 0; i < num - 1; i++) {
                finalStr += str
            }
            result = result.slice(0, start - numLength) + finalStr + result.slice(i + 1)
            i = i - (i - start  + 1) - numLength
        }
    }
    return result
};

function getNumber(s, open) {
    let numStack = []
    console.log(s, open)
    for(let i = open - 1; i >= 0; i --) {
        if(/[0-9]/.test(s[i])) {
            numStack.push(s[i])
        } else {
            break
        }
    }
    let numString = ""
    let numLength = numStack.length
    while(numStack.length) {
        numString += numStack.pop()
    }
    return [Number(numString), numLength]
}