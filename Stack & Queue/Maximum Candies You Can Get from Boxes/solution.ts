function maxCandies(status: number[], candies: number[], keys: number[][], containedBoxes: number[][], initialBoxes: number[]): number {
    let result = 0
    let keyMap = new Set() // Keys we are currently have
    let boxs = [...initialBoxes] // Box we are currently have
    
    let getAll = (box: number) => { // Get all items inside the box
        for(let key of keys[box]) {
            keyMap.add(key)
        }
        result += candies[box]
        boxs.push(...containedBoxes[box])
    }
    
    let useKey = () => { // Use all the key we can
        let changed = false // If we open at least a box => true
        for(let box of boxs) {
            if(keyMap.has(box)) {
                changed = true
                status[box] = 1
                keyMap.delete(box)
            }
        }
        return changed
    }
    
    while(true) { // Loop until nothing change
        let changed = false
        let remainingBoxs = []
        changed = useKey()
        for(let box of boxs) {
            if(status[box] === 1) {
                changed = true
                getAll(box)
            } else {
                remainingBoxs.push(box)
            }
        }
        boxs = remainingBoxs
        if(!changed) break // If we cannot use any key or open any box => break
    }
    
    return result
};