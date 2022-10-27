function largestOverlap(img1: number[][], img2: number[][]): number {
    let arr1 = [];
    let arr2 = [];
    let result = 0;
    for(let i = 0; i < img2.length; i++) {
        for(let j = 0; j < img2[0].length; j++) {
            if(img1[i][j] === 1) arr1.push([i,j])
            if(img2[i][j] === 1) arr2.push([i,j]);
        }
    }
    if(!arr1.length || !arr2.length) return 0;
    let map = new Map();
    for(let ele1 of arr1) {
        for(let ele2 of arr2) {
            let key = `${ele1[0]-ele2[0]}-${ele1[1]-ele2[1]}`
            map.set(key, (map.get(key) || 0) + 1);
        }
    }
    for(let value of map.values()) {
        result = Math.max(result, value)
    }
    
    return result;
};
