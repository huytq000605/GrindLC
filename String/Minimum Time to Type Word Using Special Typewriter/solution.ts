function minTimeToType(word: string): number {
    let result = 0
    let current = "a"
    for(let letter of word) {
        let distance = Math.abs(letter.charCodeAt(0) - current.charCodeAt(0))
        distance = Math.min(distance, 26 - distance)
        result += distance
        result++
        current = letter
    }
    return result
};