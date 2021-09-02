var widthOfBinaryTree = function(root) {
    if(!root) return 0
    let minLevel = []
    let result = 1n
    let dfs = (current, level, position) => {
        if(!current) return
        if(minLevel[level] === undefined) minLevel[level] = position
        if(position - minLevel[level] + 1n > result) {
            result = position - minLevel[level] + 1n
        }
        dfs(current.left, level + 1, position * 2n + 1n)
        dfs(current.right, level + 1, position * 2n + 2n)
    }
    dfs(root, 0, 0n)
    return Number(result)
};