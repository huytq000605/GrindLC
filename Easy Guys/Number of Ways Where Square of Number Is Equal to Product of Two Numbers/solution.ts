function numTriplets(nums1: number[], nums2: number[]): number {
    let prod2 = new Map()
    let prod1 = new Map()
    for(let j = 0; j < nums2.length - 1; j++) {
        for(let k = j + 1; k < nums2.length; k++) {
            let product = nums2[j] * nums2[k]
            prod2.set(product, (prod2.get(product) || 0) + 1)
        }
    }
    
    for(let j = 0; j < nums1.length - 1; j++) {
        for(let k = j + 1; k < nums1.length; k++) {
            let product = nums1[j] * nums1[k]
            prod1.set(product, (prod1.get(product) || 0) + 1)
        }
    }
    
    let result = 0
    for(let i = 0; i < nums1.length; i++) {
        let square = nums1[i] * nums1[i]
        result += prod2.get(square) || 0
    }
    
    for(let i = 0; i < nums2.length; i++) {
        let square = nums2[i] * nums2[i]
        result += prod1.get(square) || 0
    }
    
    return result
};