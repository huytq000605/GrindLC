function minSteps(n: number): number {
    let result = 0
    for(let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
        while(n % i === 0) {
            result += i
            n = Math.floor(n / i)
        }
    }
    if(n > 1) {
        result += n
    }
    return result
};
