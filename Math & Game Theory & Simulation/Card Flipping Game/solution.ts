function flipgame(fronts: number[], backs: number[]): number {
    let result = 0
    let map = new Map()
    let arr = []
    for(let i = 0; i < fronts.length; i++) {
        if(fronts[i] === backs[i]) {
            map.set(fronts[i], true)
        }
        arr.push(fronts[i])
        arr.push(backs[i])
    }
    arr.sort((a,b) => a-b)
    for(let i = 0; i < arr.length; i++) {
        if(!map.has(arr[i])) {
            return arr[i]
        }
    }
    return 0
    
};