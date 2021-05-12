function longestPalindrome(s: string): string {
    let result = "";
    for (let i = 0; i < s.length; i++) {
        let compare = findingLongestPalidrome(s, i, i);
        if (compare.length > result.length) result = compare;
        compare = findingLongestPalidrome(s, i, i + 1);
        if (compare.length > result.length) result = compare;
    }
    return result;
}

function findingLongestPalidrome(
    str: string,
    left: number,
    right: number
): string {
    while (str[left] === str[right] && left >= 0 && right < str.length) {
        left--;
        right++;
    }
    return str.substring(left + 1, right); // substring function get all from args[0] till args[1];
}
