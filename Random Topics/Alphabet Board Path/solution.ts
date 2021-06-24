function alphabetBoardPath(target: string): string {
    let alphabet = [["a", "b","c","d","e"], ["f","g","h","i","j"], ["k", "l", "m", "n", "o"], ["p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y"], ["z"]]
    let cache = new Map()
    let alphabetMap = new Map()
    for(let i = 0; i < alphabet.length; i++) {
        for(let j = 0; j < alphabet[i].length; j++) {
            alphabetMap.set(alphabet[i][j], [i,j])
        }
    }
    let result = ""
    let current = [0, 0]
    for(let i = 0; i < target.length; i++) {
        let destination = alphabetMap.get(target[i])
        if(target[i] === "z" && target[i-1] !== "z") {
            let dest = alphabetMap.get("u")
            result += makePath(current[0], current[1], dest[0], dest[1], cache, true)
            result += makePath(dest[0], dest[1], destination[0], destination[1], cache)
        } else if(target[i - 1] === "z" && target[i] !== "z") {
            let dest = alphabetMap.get("u")
            result += makePath(current[0], current[1], dest[0], dest[1], cache, true)
            result += makePath(dest[0], dest[1], destination[0], destination[1], cache)
        } else{
            result += makePath(current[0], current[1], destination[0], destination[1], cache)
        }
        current[0] = destination[0]
        current[1] = destination[1]
    }
    return result
};

function makePath(currentRow, currentCol, targetRow, targetCol, cache, middle = false) {
    const key = JSON.stringify(`${currentRow}${currentCol}${targetRow}${targetCol}${middle}`)
    if(cache.has(key)) {
        return cache.get(key)
    }
    if(currentRow === targetRow && currentCol === targetCol) {
        if(!middle) {
          return "!"  
        } else {
            return ""
        }
            
    }
    if(currentRow < targetRow) {
        cache.set(key, "D" + makePath(currentRow + 1, currentCol, targetRow, targetCol, cache, middle))
        return cache.get(key)
    }
    if(currentRow > targetRow) {
        cache.set(key, "U" + makePath(currentRow - 1, currentCol, targetRow, targetCol, cache, middle))
        return cache.get(key)
    }
    if(currentCol < targetCol) {
        cache.set(key, "R" + makePath(currentRow, currentCol + 1, targetRow, targetCol, cache, middle))
        return cache.get(key)
    }
    if(currentCol > targetCol) {
        cache.set(key, "L" + makePath(currentRow, currentCol - 1, targetRow, targetCol, cache, middle))
        return cache.get(key)
    }
    
}