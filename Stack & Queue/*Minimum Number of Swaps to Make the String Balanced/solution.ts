// We keep swapping the leftest wrong position close with the rightest wrong position open
function minSwaps(s: string): number {
    let left = 0
    let right = s.length -1
    let currentOpen = 0
    let currentClose = 0
    let result = 0
    while(left < right) {
        for(; left < right; left++) {
            if(s[left] === "[") {
                currentOpen++
            } else {
                currentOpen--
            }
            if(currentOpen === -1) break
        }
        
        if(left >= right) break
        for(; right > left; right--) {
            if(s[right] === "]") {
                currentClose++
            } else {
                currentClose--
            }
            if(currentClose === -1) break
        }
        
        result++
        currentOpen = 1
        currentClose = 1
        left++
        right--
    }
    return result
};