function interchangeableRectangles(rectangles: number[][]): number {
    let ratio = rectangles.map((e) => e[0] / e[1])
    let map = new Map()
    let result = 0
    for(let r of ratio) {
        result += map.get(r) || 0
        map.set(r, (map.get(r) || 0 ) + 1)
    }
    return result
};