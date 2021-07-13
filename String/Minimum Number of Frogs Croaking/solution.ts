function minNumberOfFrogs(croakOfFrogs: string): number {
    let result = 0
    let map = new Map()
    let idx = 0
    for(let letter of "croak") {
        map.set(letter, idx++)
    }
    let arr = [0, 0, 0, 0, 0]
    for(let letter of croakOfFrogs) {
        if(!map.has(letter)) return -1
        
        if(letter == "c") {
            arr[map.get(letter)] += 1
            result = Math.max(result, arr[map.get(letter)])
        } else {
            if(arr[map.get(letter) - 1] <= arr[map.get(letter)]) return -1
            arr[map.get(letter)] += 1
        }
        if(letter as any == "k") {
            for(let i = 0; i < arr.length; i++) {
                arr[i] -= 1
            }
        }
    }
    for(let num of arr) {
        if(num !== 0) return -1
    }
    return result
    
};