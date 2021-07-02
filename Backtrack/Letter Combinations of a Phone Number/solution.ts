function letterCombinations(digits: string): string[] {
    if(digits.length === 0) {
        return []
    }
    let map = new Map()
    map.set("2", ["a","b","c"])
    map.set("3", ["d","e","f"])
    map.set("4", ["g","h","i"])
    map.set("5", ["j","k","l"])
    map.set("6", ["m","n","o"])
    map.set("7", ["p","q","r","s"])
    map.set("8", ["t","u","v"])
    map.set("9", ["w","x","y","z"])
    let result = []
    helper(digits, 0, map, "", result)
    return result
};

function helper(digits, index, map, current, result) {
    if(index === digits.length) {
        result.push(current)
        return
    }
    for(let letter of map.get(digits[index])) {
        helper(digits, index + 1, map, current + letter, result)
    }
}

