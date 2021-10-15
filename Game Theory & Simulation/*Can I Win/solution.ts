function canIWin(maxChoosableInteger: number, desiredTotal: number): boolean {
    if(desiredTotal === 0) return true
    let sum = (maxChoosableInteger + 1) * (maxChoosableInteger) / 2
    if(sum < desiredTotal) return false
    let nums = Array(maxChoosableInteger + 1).fill(1)
    let dp = new Map()
	 // If this player can force win => return true
	 // If dont return false
    let canThisPlayerWin = (desiredTotal) => {        
		if(desiredTotal <= 0) {
            return false
        }
        let key = nums.toString()
        if(dp.has(key)) {
            return dp.get(key)
        }
        for(let i = 1; i <= maxChoosableInteger; i++) {
            if(nums[i] === 0) continue
            nums[i] = 0
            if(!canThisPlayerWin(desiredTotal - i)) {
                nums[i] = 1
                dp.set(key, true)
                return true
            }
            nums[i] = 1
        }
        dp.set(key, false)
        return false
        
    }
    return canThisPlayerWin(desiredTotal)
};