function compress(chars: string[]): number {
    let count = 1
    let pointer = 0
    for(let i = 1; i < chars.length; i++) {
        if(chars[i] !== chars[i - 1]) {
            if(count === 1) {
                chars[pointer++] = chars[i - 1] 
            } else {
                chars[pointer++] = chars[i - 1]
                let pushed = String(count)
                let len = pushed.length
                for(let j = 0; j < pushed.length; j++) {
                    chars[pointer++] = pushed[j]
                }
                
            }
            count = 1
            continue
        }
        if(chars[i] === chars[i - 1]) {
            count++
        }
    }
    if(count === 1) {
        chars[pointer++] = chars[chars.length - 1] 
    } else {
        chars[pointer++] = chars[chars.length - 1]
        let pushed = String(count)
        let len = pushed.length
        for(let j = 0; j < pushed.length; j++) {
            chars[pointer++] = pushed[j]
        }
    }
    return pointer
};