function maxArea(height: number[]): number {
    let start = 0;
    let end = height.length - 1;
    let result = 0;
    while(start < end) {
        result = Math.max(result, (end-start) * Math.min(height[start], height[end]) )
        if(height[start] < height[end]) {
            start++
        } else {
            end--
        }
    }
    return result
    
};