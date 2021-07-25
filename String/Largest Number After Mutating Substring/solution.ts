function maximumNumber(num: string, change: number[]): string {
    let result = ""
    let j = 0
    outer:
    for(let i = 0; i < num.length; i++) {
        if(change[num[i]] > num[i]) {
            j = i
            for(; j < num.length; j++) {
                if(change[num[j]] >= num[j]) {
                    result += change[num[j]]
                } else {
                    break outer
                }
            }
            break
        } else {
            result += num[i]
            j++
        }
    }
    while(j < num.length) {
        result += num[j]
        j++
    }
    return result
};