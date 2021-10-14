function circularArrayLoop(nums: number[]): boolean {
    let seen = new Map()
    let n = nums.length
    let dfs = (idx) => {
        if(seen.has(idx)) {
            if(seen.get(idx) === true) return false
            else return true
        }
        let nextIdx = (((idx + nums[idx]) % n) + n) % n
        if(nextIdx === idx || nums[idx] * nums[nextIdx] < 0) {
            seen.set(idx, true)
            return false
        }
        seen.set(idx, false)
        if(dfs(nextIdx)) {
            return true
        } else {
            seen.set(idx, true)
            return false
        }
    }
    for(let i = 0; i < nums.length; i++) {
        if(dfs(i)) return true
    }
    return false

};