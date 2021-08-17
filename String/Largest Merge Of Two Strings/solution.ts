function largestMerge(word1: string, word2: string): string {
    let i1 = 0
    let i2 = 0
    let result = ""
    while(i1 < word1.length || i2 < word2.length) {
        if(i1 < word1.length && (i2 >= word2.length || word1[i1] > word2[i2])) {
            result += word1[i1]
            i1++
        } else if(i2 < word2.length && (i1 >= word1.length || word2[i2] > word1[i1])) {
            result += word2[i2]
            i2++
        } else {
            if(word1.slice(i1) > word2.slice(i2)) {
                result += word1[i1]
                i1++
            } else {
                result += word2[i2]
                i2++
            }
        }
    }
    return result
};