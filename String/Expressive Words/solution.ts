function expressiveWords(s: string, words: string[]): number {
    let cmp = changeString(s)
    let result = 0
    for(let wordO of words) {
        let word = changeString(wordO)
        let stretchy = false
        if(word.length !== cmp.length) continue
        for(let i = 0; i < word.length; i++) {
            if(word[i][1] < cmp[i][1]) {
                if(cmp[i][1] >= 3) stretchy = true
                else {
                    stretchy = false
                    break
                }
            } else if(word[i][1] > cmp[i][1]) {
                stretchy = false
                break
            }
        }
        if(stretchy) result++
    }
    return result
};

function changeString(s: string) {
    let result = []
    for(let i = 0; i < s.length; i++) {
        if(i === 0) result.push([s[i], 1])
        else if(s[i] === result[result.length - 1][0]) {
            result[result.length - 1][1] += 1
        } else {
            result.push([s[i], 1])
        }
    }
    return result
}