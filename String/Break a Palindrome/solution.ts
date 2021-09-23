function breakPalindrome(palindrome: string): string {
    if(palindrome.length === 1) return ""
    for(let i = 0; i < Math.floor(palindrome.length / 2); i++) {
        if(palindrome[i] !== "a") {
            return palindrome.slice(0, i) + "a" + palindrome.slice(i + 1)
        }
    }
    return palindrome.slice(0, palindrome.length - 1) + "b"
};