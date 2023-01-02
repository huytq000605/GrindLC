function numTimesAllBlue(light: number[]): number {
    let open = Array(light.length).fill(0)
    let currentOpen = 0
    let maxOpen = 0
    let result = 0
    for(let i = 0; i < light.length; i++) {
        open[light[i]] = 1
        while(open[currentOpen + 1] === 1) {
            currentOpen++
        }
        maxOpen = Math.max(maxOpen, light[i])
        if(maxOpen === currentOpen) result++
    }
    return result
};