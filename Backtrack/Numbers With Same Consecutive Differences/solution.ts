function numsSameConsecDiff(n: number, k: number): number[] {
    let result = []
    function helper(n, current) {
        if(n === 0) {
            result.push(Number(current))
            return
        }
        if(current.length) {
            let lastNumber = Number(current[current.length - 1])
            let smaller = lastNumber - k
            let bigger = lastNumber + k
            if(smaller >= 0 && smaller <= 9) helper(n-1, current + smaller)
            if(bigger >= 0 && bigger <= 9 && bigger !== smaller) helper(n-1, current + bigger)
            
        } else {
            for(let i = 1; i <= 9; i++) {
                helper(n - 1, current + i)
            }
        }
        
    }
    helper(n, "")
    return result
};

