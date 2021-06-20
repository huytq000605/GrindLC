function numSubarraysWithSum(nums: number[], goal: number): number {
    let start = 0;
    let oneIndex = []
    let result = 0
    for(let i = 0; i < nums.length; i++) {
        
        if(nums[i] === 1) {
            oneIndex.push(i)
        }
        let sum = oneIndex.length;
        if(sum > goal) {
            start = oneIndex[0] + 1
            oneIndex.shift()
            sum--
        }
        
        if(sum === goal) {
            if(goal === 0) {
                result += i - start + 1
            } else {
                result += oneIndex[0] - start + 1
            }

        }
        
    }
    return result
};