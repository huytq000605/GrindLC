function findLUSlength(strs: string[]): number {
    let trie = {depth: 0}
    let result = -1
    let dfsWord = (idx: number, str: string, current: Record<string, any>) => {
        if(idx === str.length) return
         let letter = str[idx]
            if(!current[letter]) {
                current[letter] = {depth: current.depth + 1, appears: 1}
            } else {
                current[letter].appears++
            }
        dfsWord(idx + 1, str, current[letter])
        dfsWord(idx + 1, str, current)
    }
    for(let str of strs) {
        dfsWord(0, str, trie)
    }
    let current = trie
    let dfs = (trie) => {
        if(trie.appears && trie.appears === 1) {
            result = Math.max(result, trie.depth)
        }
        for(let key of Object.keys(trie)) {
            dfs(trie[key])
        }
    }
    dfs(trie)
    return result
};