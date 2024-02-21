function rangeBitwiseAnd(left: number, right: number): number {
    let i = 0;
    while(left !== right) {
        left >>= 1
        right >>= 1
        i++
    }
    return left << i
};
