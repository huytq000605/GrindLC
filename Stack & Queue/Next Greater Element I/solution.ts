function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    let index = new Map()
    for(let i = 0; i < nums1.length; i++) {
        index.set(nums1[i], i)
    }
    let stack = []
    let result = Array(nums1.length).fill(-1)
    for(let num of nums2) {
        while(stack.length && num > stack[stack.length - 1]) {
            let previous = stack.pop()
            if(index.has(previous)) {
                result[index.get(previous)] = num
            }
        }
        stack.push(num)
    }
    return result
};