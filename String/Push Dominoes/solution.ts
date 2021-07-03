function pushDominoes(dominoes: string): string {
    let j = -1
    let result = ["L", ...dominoes.split(""), "R"]
    for(let i = 0; i < result.length; i++) {
        if(result[i] === "R") {
            if(result[j] === "R") {
                for(let k = j + 1; k < i; k++) {
                    result[k] = "R" 
                }
            }
            j = i
        }
        if(result[i] === "L") {
            if(result[j] === "R") {
                let left = j + 1
                let right = i - 1
                while(left < right) {
                    result[left] = "R"
                    result[right] = "L"
                    left++
                    right--
                }
            }
            if(result[j] === "L") {
                for(let k = j + 1; k < i; k++) {
                    result[k] = "L"
                }
            }
            j = i
        }
    }
    return result.slice(1, result.length- 1).join("")
};