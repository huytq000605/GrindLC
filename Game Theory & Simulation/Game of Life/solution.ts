/**
 Do not return anything, modify board in-place instead.
 */
 function gameOfLife(board: number[][]): void {
	let cloneBoard = Array(board.length).fill([]).map(ele => Array(board[0].length));
	for(let i = 0; i < board.length; i++) {
			for(let j = 0; j < board[0].length; j++) {
					cloneBoard[i][j] = board[i][j]
			}
	}
	for(let i = 0; i < board.length; i++) {
			for(let j = 0; j < board[0].length; j++) {
					let count = 0;
					for(let m = -1; m < 2; m++) {
							for(let n = -1; n < 2; n++) {
									if(m == 0 && n == 0) continue;
									if(i + m < 0 || i + m >= board.length) continue;
									if(j + n < 0 || j + n >= board[0].length) continue;
									if(cloneBoard[i+m][j+n] === 1) count++;
							}
					}
					if(board[i][j]) {
							if(count < 2) board[i][j] = 0;
							else if(count >3) board[i][j] = 0;
					}
					else {
							if(count == 3) board[i][j] = 1
					}
			}
	}
};