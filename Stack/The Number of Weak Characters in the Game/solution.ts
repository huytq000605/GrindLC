function numberOfWeakCharacters(props: number[][]): number {
    let result = 0
    props.sort((a,b) => a[0] - b[0] || b[1] - a[1])
    let stack = []
    for(let prop of props) {
        let [atk, def] = prop
        while(stack.length && stack[stack.length - 1][0] < atk && stack[stack.length - 1][1] < def) {
            stack.pop()
            result++
        }
        stack.push(prop)
    }
    return result
};