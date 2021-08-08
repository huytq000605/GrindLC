function checkMove(
    board: string[][],
    rMove: number,
    cMove: number,
    color: string
): boolean {
    let top = rMove - 1 < 0 ? null : [rMove - 1, cMove];
    let bottom = rMove + 1 >= board.length ? null : [rMove + 1, cMove];
    let left = cMove - 1 < 0 ? null : [rMove, cMove - 1];
    let right = cMove + 1 >= board[0].length ? null : [rMove, cMove + 1];
    let topLeft = null;
    let bottomLeft = null;
    let topRight = null;
    let bottomRight = null;
    if (top && left) topLeft = [rMove - 1, cMove - 1];
    if (top && right) topRight = [rMove - 1, cMove + 1];
    if (bottom && left) bottomLeft = [rMove + 1, cMove - 1];
    if (bottom && right) bottomRight = [rMove + 1, cMove + 1];
    if (
        top &&
        board[top[0]][top[1]] !== color &&
        board[top[0]][top[1]] !== "."
    ) {
        for (let row = top[0] - 1; row >= 0; row--) {
            if (board[row][top[1]] === ".") break;
            if (board[row][top[1]] === color) return true;
        }
    }
    if (
        bottom &&
        board[bottom[0]][bottom[1]] !== color &&
        board[bottom[0]][bottom[1]] !== "."
    ) {
        for (let row = bottom[0] + 1; row < board[0].length; row++) {
            if (board[row][bottom[1]] === ".") break;
            if (board[row][bottom[1]] === color) return true;
        }
    }
    if (
        left &&
        board[left[0]][left[1]] !== color &&
        board[left[0]][left[1]] !== "."
    ) {
        for (let col = left[1] - 1; col >= 0; col--) {
            if (board[left[0]][col] === ".") break;
            if (board[left[0]][col] === color) return true;
        }
    }
    if (
        right &&
        board[right[0]][right[1]] !== color &&
        board[right[0]][right[1]] !== "."
    ) {
        for (let col = right[1] + 1; col < board[0].length; col++) {
            if (board[right[0]][col] === ".") break;
            if (board[right[0]][col] === color) return true;
        }
    }

    if (
        topLeft &&
        board[topLeft[0]][topLeft[1]] !== color &&
        board[topLeft[0]][topLeft[1]] !== "."
    ) {
        for (
            let change = 1;
            topLeft[0] - change >= 0 && topLeft[1] - change >= 0;
            change++
        ) {
            if (board[topLeft[0] - change][topLeft[1] - change] === ".") break;
            if (board[topLeft[0] - change][topLeft[1] - change] === color)
                return true;
        }
    }
    if (
        topRight &&
        board[topRight[0]][topRight[1]] !== color &&
        board[topRight[0]][topRight[1]] !== "."
    ) {
        for (
            let change = 1;
            topRight[0] - change >= 0 && topRight[1] + change < board[0].length;
            change++
        ) {
            if (board[topRight[0] - change][topRight[1] + change] === ".")
                break;
            if (board[topRight[0] - change][topRight[1] + change] === color)
                return true;
        }
    }
    if (
        bottomLeft &&
        board[bottomLeft[0]][bottomLeft[1]] !== color &&
        board[bottomLeft[0]][bottomLeft[1]] !== "."
    ) {
        for (
            let change = 1;
            bottomLeft[0] + change < board.length &&
            bottomLeft[1] - change >= 0;
            change++
        ) {
            if (board[bottomLeft[0] + change][bottomLeft[1] - change] === ".")
                break;
            if (board[bottomLeft[0] + change][bottomLeft[1] - change] === color)
                return true;
        }
    }
    if (
        bottomRight &&
        board[bottomRight[0]][bottomRight[1]] !== color &&
        board[bottomRight[0]][bottomRight[1]] !== "."
    ) {
        for (
            let change = 1;
            bottomRight[0] + change < board.length &&
            bottomRight[1] + change < board[0].length;
            change++
        ) {
            if (board[bottomRight[0] + change][bottomRight[1] + change] === ".")
                break;
            if (
                board[bottomRight[0] + change][bottomRight[1] + change] ===
                color
            )
                return true;
        }
    }
    return false;
}
