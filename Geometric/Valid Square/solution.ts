function validSquare(p1: number[], p2: number[], p3: number[], p4: number[]): boolean {
    let arr = [p1, p2, p3, p4]
    if(p1[0] === p2[0] && p1[1] === p2[1]) return false
    arr.sort((a,b) => a[0] - b[0] || a[1] - b[1])
    let edge = distance(arr[0], arr[1])
    for(let i = 0; i < arr.length; i++) {
        for(let j = i + 1; j < arr.length; j++) {
            if( (i === 0 && j === 3) || (i === 1 && j === 2) ) {
                let dist = distance(arr[i], arr[j])
                if(dist !== edge * 2) return false
                else continue
            }
            if(distance(arr[i], arr[j]) !== edge) {
                return false
            }
        }
    }
    return true
};

function distance (p1, p2) {
    return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])
}