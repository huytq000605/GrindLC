function pathInZigZagTree(label: number): number[] {
    let levelOfLabel = 1
    while((1 << levelOfLabel) - 1 < label) {
        levelOfLabel++
    }
    let result = []
    while(label >= 1) {
        let start = 1 << (levelOfLabel - 1)
        let end = (1 << levelOfLabel) - 1
        result.push(label)
        if(levelOfLabel % 2 === 0) { // is fake => find real
            let realLabel = start + (end - label)
            label = Math.floor(realLabel / 2)
        } else { // is real => find fake
            let fakeLabel = start + (end - label)
            label = Math.floor(fakeLabel / 2)
        }
        levelOfLabel--
    }
    
    let left = 0
    let right = result.length - 1
    while(left < right) {
        [result[left], result[right]] = [result[right], result[left]];
        left++
        right--
    }
    
    return result
};