function chalkReplacer(chalk: number[], k: number): number {
    let sum = 0
    for(let num of chalk) {
        sum += num
    }
    k = k % sum
    for(let [index, num] of chalk.entries()) {
        if(k < num) return index
        k -= num
    }
    return 0
};