function closestCost(baseCosts: number[], toppingCosts: number[], target: number): number {
    let result = undefined
    
    function check(newCurrent: number, current: number) {
        let newDiff = Math.abs(target - newCurrent)
        let diff = Math.abs(target - current)
        if(newDiff < diff || (newDiff === diff && newCurrent < current)) {
            return true
        } else {
            return false
        }
    }
    
    function helper(current: number, lastTopping: number) {
        let result = current
        if(lastTopping !== toppingCosts.length - 1  && current < target) {
            for(let j = 0; j <= 2; j++) {
                let newCurrent = helper(current + toppingCosts[lastTopping + 1] * j, lastTopping + 1)
                if(newCurrent === target) {
                    return target
                }
                if(check(newCurrent, result)) {
                    result = newCurrent
                }
            }
        } 
        return result
    }
    
    for(let i = 0; i < baseCosts.length; i++) {
        let cmp = helper(baseCosts[i], -1)
        if(cmp === target) {
            return target
        }
        if(!result || check(cmp, result)) {
            result = cmp
        }
    }
    return result
    
};

