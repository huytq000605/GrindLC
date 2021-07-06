function triangleNumber(nums: number[]): number {
    nums.sort((a,b) => a-b)
    let result = 0
    for(let edge1 = nums.length - 1; edge1 >= 2; edge1--) { // Choose edge1 is the maximum edge
        let edge2 = 0
        let edge3 = edge1 -1
        while(edge2 < edge3) {
            if(nums[edge2] + nums[edge3] > nums[edge1]) {
                result += edge3 - edge2 // If this is valid then edge2 can be everything from edge2 to edge3 - 1
                edge3--
            } else {
                edge2++
            }
        }
    } 
    return result
};