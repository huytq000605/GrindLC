function maxSumTwoNoOverlap(A: number[], L: number, M: number): number {
    let prefix = [A[0]]
    for(let i = 1; i < A.length; i++) {
        prefix[i] = prefix[i-1] + A[i];
    }
    return Math.max(maxSum(prefix, L, M), maxSum(prefix, M, L))
}

function maxSum(prefix: number[], m: number, n: number): number {
    let maxFirst = prefix[m-1];
    let maxBoth = prefix[m+n-1];
    for(let i = m + n; i < prefix.length; i++) {
        maxFirst = Math.max(maxFirst, prefix[i-n] - prefix[i-m-n]);
        maxBoth = Math.max(maxBoth, prefix[i] - prefix[i-n] + maxFirst);
    }
    return maxBoth
}