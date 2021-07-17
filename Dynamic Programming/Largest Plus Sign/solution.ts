function orderOfLargestPlusSign(n: number, mines: number[][]): number {
    let left = Array(n)
        .fill(0)
        .map(() => Array(n).fill(0));
    let up = Array(n)
        .fill(0)
        .map(() => Array(n).fill(0));
    let down = Array(n)
        .fill(0)
        .map(() => Array(n).fill(0));
    let right = Array(n)
        .fill(0)
        .map(() => Array(n).fill(0));

    let mineSet = new Set();
    for (let mine of mines) {
        const key = `${mine[0]},${mine[1]}`;
        mineSet.add(key);
    }

    fillUp(up, mineSet);
    fillLeft(left, mineSet);
    fillRight(right, mineSet);
    fillDown(down, mineSet);

    let result = 0;
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            if (!mineSet.has(`${row},${col}`)) {
                let res = Math.min(
                    up[row][col],
                    down[row][col],
                    left[row][col],
                    right[row][col]
                );
                result = Math.max(result, res);
            }
        }
    }
    return result;
}

function fillUp(matrix, mineSet) {
    for (let col = 0; col < matrix.length; col++) {
        for (let row = 0; row < matrix.length; row++) {
            if (mineSet.has(`${row},${col}`)) {
                matrix[row][col] = 0;
            } else {
                if (row === 0) {
                    matrix[row][col] = 1;
                } else {
                    matrix[row][col] = matrix[row - 1][col] + 1;
                }
            }
        }
    }
}

function fillDown(matrix, mineSet) {
    for (let col = 0; col < matrix.length; col++) {
        for (let row = matrix.length - 1; row >= 0; row--) {
            if (mineSet.has(`${row},${col}`)) {
                matrix[row][col] = 0;
            } else {
                if (row === matrix.length - 1) {
                    matrix[row][col] = 1;
                } else {
                    matrix[row][col] = matrix[row + 1][col] + 1;
                }
            }
        }
    }
}

function fillLeft(matrix, mineSet) {
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix.length; col++) {
            if (mineSet.has(`${row},${col}`)) {
                matrix[row][col] = 0;
            } else {
                if (col === 0) {
                    matrix[row][col] = 1;
                } else {
                    matrix[row][col] = matrix[row][col - 1] + 1;
                }
            }
        }
    }
}

function fillRight(matrix, mineSet) {
    for (let row = 0; row < matrix.length; row++) {
        for (let col = matrix.length - 1; col >= 0; col--) {
            if (mineSet.has(`${row},${col}`)) {
                matrix[row][col] = 0;
            } else {
                if (col === matrix.length - 1) {
                    matrix[row][col] = 1;
                } else {
                    matrix[row][col] = matrix[row][col + 1] + 1;
                }
            }
        }
    }
}
