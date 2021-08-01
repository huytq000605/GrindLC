function lexicalOrder(n: number): number[] {
    let result = []
    function helper(current) {
        if(current > n) {
            return
        }
        result.push(current)
        helper(current * 10)
        if(current % 10 !== 9) {
            helper(current + 1)
        }
    }
    helper(1)
    return result
    
};

