function countVowels(word: string): number {
    let result = 0
    let vowels = "ueoai"
    for(let i = 0; i < word.length; i++) {
        if(vowels.indexOf(word[i]) !== -1) {
            result += (i+1) * (word.length - i)
        }
    }
    return result
};