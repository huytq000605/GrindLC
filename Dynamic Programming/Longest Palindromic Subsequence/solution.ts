function longestPalindromeSubseq(s: string): number {
    let map = new Map()
    return longestPalindrome(s, 0, s.length - 1, map)
}

function longestPalindrome(s: string, left: number, right: number, map):number {
    const key = `${left}-${right}`
    if(map.has(key)) {
        return map.get(key)
    }
    if(left > right) {
        return 0
    }
    if(left == right) {
        return 1
    }
    let plus = 0
    if(s[left] == s[right]) {
        map.set(key, 2 + longestPalindrome(s, left + 1, right - 1, map))
        return map.get(key)
    }
    const increaseLeft = longestPalindrome(s, left + 1, right, map)
    const decreaseRight = longestPalindrome(s, left, right - 1, map)
    map.set(key, Math.max(increaseLeft, decreaseRight))
    return map.get(key)
}
