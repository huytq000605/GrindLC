/*
1) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = (x[i] - x[j]|) + (y[i] - y[j]) + (i-j) = (x[i] + y[i] + i) - (x[j] + y[j] + j)
2) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = (x[i] - x[j]|) - (y[i] - y[j]) + (i-j) = (x[i] - y[i] + i) - (x[j] - y[j] + j)
3) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = -(x[i] - x[j]|) + (y[i] - y[j]) + (i-j) = (-x[i] + y[i] + i) - (-x[j] + y[j] + j)
4) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = -(x[i] - x[j]|) - (y[i] - y[j]) + (i-j) = (-x[i] - y[i] + i) - (-x[j] - y[j] + j)
5) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = (x[i] - x[j]|) + (y[i] - y[j]) - (i-j) = (x[i] + y[i] - i) - (x[j] + y[j] - j)
6) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = (x[i] - x[j]|) - (y[i] - y[j]) - (i-j) = (x[i] - y[i] - i) - (x[j] - y[j] - j)
7) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = -(x[i] - x[j]|) + (y[i] - y[j]) - (i-j) = (-x[i] + y[i] - i) - (-x[j] + y[j] - j)
8) |x[i] - x[j]| + |y[i] - y[j]| + |i-j| = -(x[i] - x[j]|) - (y[i] - y[j]) - (i-j) = (-x[i] - y[i] - i) - (-x[j] - y[j] - j)
So 1 is same with 8, 2 is same with 7, 3 is same with 6, 4 is same with 5
i and j is just the index so doesn't matter
*/

function maxAbsValExpr(arr1: number[], arr2: number[]): number {
    let a1 = Array(arr1.length).fill(0)
    let a2 = Array(arr1.length).fill(0)
    let a3 = Array(arr1.length).fill(0)
    let a4 = Array(arr1.length).fill(0)
    for(let i = 0; i < arr1.length; i++) {
        a1[i] = arr1[i] + arr2[i] + i
        a2[i] = arr1[i] - arr2[i] + i
        a3[i] = -arr1[i] + arr2[i] + i
        a4[i] = -arr1[i] - arr2[i] + i
    }
    let m1 = find(a1)
    let m2 = find(a2)
    let m3 = find(a3)
    let m4 = find(a4)
    return Math.max(m1, m2, m3, m4)
    
};

function find(arr: number[]) {
    let min = Number.MAX_SAFE_INTEGER
    let max = Number.MIN_SAFE_INTEGER
    for(let i = 0; i < arr.length; i++) {
        min = Math.min(min, arr[i])
        max = Math.max(max, arr[i])
    }
    return max - min
}