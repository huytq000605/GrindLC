function reverseOnlyLetters(s: string): string {
    let arr = []
    for(let c of s) {
        arr.push(c)
    }
    let left = 0
    let right = arr.length - 1
    while(left < right) {
        while(left < right && !( (arr[left] >= "A" && arr[left] <= "Z") || (arr[left] >= "a" && arr[left] <= "z") ) ) {
          left++  
        }
            
        while(left < right && !( (arr[right] >= "A" && arr[right] <= "Z") || (arr[right] >= "a" && arr[right] <= "z") ) ) {
            right--
        }
            
        if(left < right) {
            [arr[left], arr[right]] = [arr[right], arr[left]]
            left++
            right--
        }
    }
    return arr.join("")
};