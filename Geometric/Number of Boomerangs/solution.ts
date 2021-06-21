function numberOfBoomerangs(points: number[][]): number {
    if(points.length < 3) {
        return 0
    }
    let result = 0;
    for(let point of points) {
        let i = point;
        let freq = new Map()
        for(let k of points) {
            if(k[0] === i[0] && k[1] === i[1]) {
                continue
            }
            
            let distance = Math.pow(i[0] - k[0], 2) + Math.pow(i[1] - k[1], 2)
            freq.set(distance, ( freq.get(distance) || 0 ) + 1)
        }
        for(let numOfSameDistance of freq.values() ) {
                result += numOfSameDistance * (numOfSameDistance - 1) // 2 permutations of N = N! / (N-2)! = N * ( N - 1) 
            }
    }
    return result
};