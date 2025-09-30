# Pascal Triangle

## Example: 2221. Find Triangular Sum of an Array

// 1 2 3 4 5
// (1+2) + (2+3) + (3+4) + (4+5)
// (1+2+2+3) + (2+3+3+4) + (3+4+4+5)
// (1+2+2+2+3+3+3+4) + (2+3+3+3+4+4+4+5)

// freq 
// 1 1 1 1 1 
// 1 2 2 2 1
// 1 3 4 3 1
// 1 4 6 4 1
// values[i] = (n-1)Ci for i in range(n)
// lazy calculate nCk = (n-1)C(k-1) + (n-1)Ck
