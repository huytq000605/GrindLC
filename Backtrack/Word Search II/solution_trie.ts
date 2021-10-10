function findWords(board: string[][], words: string[]): string[] {
    let trie = {}
    for(let word of words) {
        insertWordToTrie(trie, word)
    }
    let dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    let result = []
    let dfs = (i: number, j: number, current: Record<string, any>) => {
        let letter = board[i][j]
        if(!current[letter]) return
        current = current[letter]
        if(current.word && current.word !== "") {
            result.push(current.word)
            current.word = ""
        }
        board[i][j] = "#"
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row < 0 || col < 0 || row >= board.length || col >= board[0].length || board[row][col] === "#") continue
            dfs(row, col, current)
        }
        board[i][j] = letter
    }
    
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j < board[0].length; j++) {
            dfs(i, j, trie)
        }
    }
    return result
};

function insertWordToTrie(trie: Record<string, any>, word: string) {
	let current = trie
	for(let letter of word) {
		if(!current[letter]) current[letter] = {}
		current = current[letter]
	}
	current.word = word
}