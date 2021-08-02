function isPossible(nums: number[]): boolean {
    let freq = new Map()
    for(let i = 0; i < nums.length; i++) {
        if(!freq.has(nums[i])) freq.set(nums[i], [])
        freq.get(nums[i]).push(i)
    }
    let indexUsed = new Set()
    for(let i = 0; i < nums.length; i++) {
        if(indexUsed.has(i)) continue
        
        let num = nums[i]
        freq.get(num).shift()
        let prev = freq.get(num).length
        let count = 1
        
        while(freq.has(num + 1) && freq.get(num + 1).length > 0) {
            if(prev >= freq.get(num + 1).length && count >= 3) break
            indexUsed.add(freq.get(num + 1).shift())
            prev = Math.max(prev, freq.get(num+1).length)
            count++
            num++
        }
        
        if(count < 3) return false
    }
    return true
};
