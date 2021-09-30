function updateMatrix(mat: number[][]): number[][] {
    let result = Array(mat.length)
        .fill(0)
        .map(() => Array(mat[0].length).fill(Number.MAX_SAFE_INTEGER));
    for (let row = 0; row < mat.length; row++) {
        for (let col = 0; col < mat[0].length; col++) {
            if (mat[row][col] === 0) {
                result[row][col] = 0;
            } else {
                if (row > 0)
                    result[row][col] = Math.min(
                        result[row][col],
                        1 + result[row - 1][col]
                    );
                if (col > 0)
                    result[row][col] = Math.min(
                        result[row][col],
                        1 + result[row][col - 1]
                    );
            }
        }
    }

    for (let row = mat.length - 1; row >= 0; row--) {
        for (let col = mat[0].length - 1; col >= 0; col--) {
            if (row < mat.length - 1)
                result[row][col] = Math.min(
                    result[row][col],
                    1 + result[row + 1][col]
                );
            if (col < mat[0].length - 1)
                result[row][col] = Math.min(
                    result[row][col],
                    1 + result[row][col + 1]
                );
        }
    }

    return result;
}
