function minimumMountainRemovals(nums: number[]): number {
    let LIS = (arr) => {
        let lens = Array(arr.length).fill(1)
        let current = []
        for(let i = 0; i < arr.length; i++) {
            if(!current.length || arr[i] > current[current.length - 1]) {
                current.push(arr[i])
            } else {
                let min = 0
                let max = current.length -1
                while(min < max) {
                    let mid = min + Math.floor((max - min) / 2)
                    if(current[mid] > arr[i]) {
                        max = mid
                    } else {
                        min = mid + 1
                    }
                }
                current[min] = arr[i]
                
            }
            lens[i] = current.length
        }
        return lens
        
    }
    
    let left = LIS(nums)
    let right = LIS(nums.reverse()).reverse()
    let longestMoutain = 0
    for(let mid = 1; mid < nums.length - 1; mid++) {
        if(left[mid] > 1 && right[mid] > 1)
            longestMoutain = Math.max(longestMoutain, left[mid] + right[mid] - 1)
    }
    return nums.length - longestMoutain
};