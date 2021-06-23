function minDistance(word1: string, word2: string): number {
    let cache = new Map()
    return helper(word1, word2, 0, 0, cache)
};

function helper(word1: string, word2: string, i: number, j: number, cache: Map<string, number>) {
    if(i === word1.length) {
        return word2.length - j
    }
    if(j === word2.length) {
        return word1.length - i
    }
    const key = `${i}-${j}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    if(word1[i] === word2[j]) {
        cache.set(key, helper(word1, word2, i + 1, j + 1, cache))
        return cache.get(key)
    }
    let deleteWord1 = 1 + helper(word1, word2, i + 1, j , cache)
    let deleteWord2 = 1 + helper(word1, word2, i, j + 1, cache)
    cache.set(key, Math.min(deleteWord1, deleteWord2))
    return cache.get(key)
}