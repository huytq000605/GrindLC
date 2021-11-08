function palindromePairs(words: string[]): number[][] {
    let dict = new Map()
    let result = []
    for(let i = 0; i < words.length; i++) {
        if(words[i] === "") {
            for(let j = 0; j < words.length; j++) {
                if(j === i) continue
                if(isPalindrome(words[j])) result.push([i, j], [j, i])
            }
            continue
        }
        dict.set(words[i], i)
    }
    for(let i = 0; i < words.length; i++) {
        const word = words[i]
        for(let boundary = 0; boundary < word.length; boundary++) {
            let middle = word.slice(0, boundary)
            if(isPalindrome(middle)) {
                let suffix = word.slice(boundary)
                let prefix = reverseString(suffix)
                if(dict.has(prefix)) {
                    let prefixIdx = dict.get(prefix)
                    if(prefixIdx === i) continue
                    result.push([prefixIdx, i])
                } 
            }
            
            middle = word.slice(boundary)
            if(isPalindrome(middle)) {
                let prefix = word.slice(0, boundary)
                let suffix = reverseString(prefix)
                if(dict.has(suffix)) {
                    let suffixIdx = dict.get(suffix)
                    if(suffixIdx === i) continue
                    result.push([i, suffixIdx])
                }
            }
            
        }
    }
    return result
};

function reverseString(word) {
    let result = ""
    for(let i = word.length - 1; i >= 0; i--) {
        result += word[i]
    }
    return result
}

function isPalindrome(word) {
    let left = 0
    let right = word.length - 1
    while(left < right) {
        if(word[left] !== word[right]) return false
        left++
        right--
    }
    return true
}