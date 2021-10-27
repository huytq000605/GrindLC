function countValidWords(sentence: string): number {
    let currentWord = ""
    let result = 0
    for(let l of sentence) {
        if(l === " ") {
            if(currentWord.length) {
                if(isValid(currentWord)) result++
            }
            currentWord = ""
        } else {
            currentWord += l
        }
    }
    if(currentWord.length) {
        if(isValid(currentWord)) result++
    }
    return result
};


function isValid(word) {
    let seen = false
    for(let i = 0; i < word.length; i++) {
        let l = word[i]
        if(l >= "0" && l <= "9") return false
        if(l === "!" || l === "." || l === ",") {
            if(i !== word.length - 1) return false
        }
        if(l === "-") {
            if(seen) return false
            seen = true
            if(i === 0 || i === word.length - 1) return false
            if(!(word[i - 1] >= "a" && word[i-1] <= "z") || !(word[i + 1] >= "a" && word[i-1] <= "z")) return false
        }
    }
    return true
}