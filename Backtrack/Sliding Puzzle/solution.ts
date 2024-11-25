function slidingPuzzle(board: number[][]): number {
    let state = []
    for(let row = 0; row < 2; row++) {
        for(let col = 0; col < 3; col++) {
            state.push(board[row][col])
        }
    }
    let map = new Map()
    map.set(0, [1, 3])
    map.set(1, [0, 2, 4])
    map.set(2, [1, 5])
    map.set(3, [0, 4])
    map.set(4, [1, 3, 5])
    map.set(5, [2, 4])
    let seen = new Set()
    let queue: any = [[state, 0]]
    while(queue.length) {
        let [current, step] = queue.shift()  
        if(check(current)) return step
        
        let key = JSON.stringify(current)
        if(seen.has(key)) continue
        seen.add(key)
        
        let movingPoint = current.indexOf(0)
        for(let next of map.get(movingPoint)) {
            [current[next], current[movingPoint]] = [current[movingPoint], current[next]];
            queue.push([[...current], step + 1]);
            [current[next], current[movingPoint]] = [current[movingPoint], current[next]];
        }
    }
    return -1
};

function check(arr) {
    for(let i = 0;i < arr.length; i++) {
        if(i === arr.length-1) {
            if(arr[i] === 0) return true
            else return false
        }
        if(arr[i] !== i + 1) return false
    }
    return false
}