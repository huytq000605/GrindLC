function queryString(S: string, N: number): boolean {
    let memo = {};
    const decToBin = (num: number) => {
        if(num === 1) {
            return "1"
        }
        if(num === 0) {
            return ""
        }
        if(num in memo) {
            return memo[num]
        }
        memo[num] = decToBin(Math.floor(num/2)) + String(num%2)
        return memo[num]
    }
    for(let i = 1; i <= N; i++) {
        if(S.indexOf(decToBin(i)) === -1) return false;
    }
    return true;

};
