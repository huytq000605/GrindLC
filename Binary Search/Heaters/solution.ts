function findRadius(houses: number[], heaters: number[]): number {
    heaters.sort((a,b) => a-b)
    let result = 0
    for(let house of houses) {
        let res = Number.MAX_SAFE_INTEGER // Warm this house
        let min = 0
        let max = heaters.length - 1
        while(min < max) { // Find the nearest smaller 
            let mid = min + Math.ceil((max - min + 1) / 2)
            if(heaters[mid] === house) {
                min = mid
                break
            }
            if(heaters[mid] > house) {
                max = mid - 1
            } else {
                min = mid
            }
        }
        res = Math.min(res, Math.abs(heaters[min] - house))
        min = 0
        max = heaters.length - 1
        while(min < max) { // Find the nearest bigger
            let mid = min + Math.floor((max - min) / 2)
            if(heaters[mid] === house) {
                min = mid
                break
            }
            if(heaters[mid] > house) {
                max = mid
            } else {
                min = mid + 1
            }
        }
        res = Math.min(res, Math.abs(heaters[min] - house))
        result = Math.max(result, res)
    }
    return result
    
};