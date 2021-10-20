function minCharacters(a: string, b: string): number {
    let counterA = counter(a)
    let counterB = counter(b)
    let swapA = a.length - Math.max(...counterA)
    let swapB = b.length - Math.max(...counterB)
    let result = swapA + swapB // third choice
    for(let i = 1; i < 26; i++) { // i cannot = 0 because have no letter
        result = Math.min(result, calculate(counterA, counterB, i), calculate(counterB, counterA, i))
    }
    return result
    
};

function calculate(arr1: number[], arr2: number[], letter: number) { // Every letter of arr1 is < letter, every letter of arr2 is >= letter
    let result = 0
    for(let i = letter; i < 26; i++) {
        result += arr1[i]
    }
    for(let i = 0; i < letter; i++) {
        result += arr2[i]
    }
    return result
}

function counter(s: string) {
    let arr = Array(26).fill(0)
    for(let i = 0; i < s.length; i++) {
        arr[s.charCodeAt(i) - "a".charCodeAt(0)]++
    }
    return arr
}