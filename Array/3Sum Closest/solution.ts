function threeSumClosest(nums: number[], target: number): number {
    let result = 0;
    let distance = Number.MAX_SAFE_INTEGER;
    nums.sort((a,b) => a-b);
    for(let i = 0; i < nums.length; i++) {
        const picked = nums[i];
        const remaining = target - nums[i];
        let first = i+1;
        let last = nums.length - 1;
        while(first < last) {

            const total = nums[first] + nums[last];
            if(total - remaining === 0) return picked + total ;
            if(Math.abs(total - remaining) < distance) {
                distance = Math.abs(total - remaining);
                result = picked + total;
            }
            if(total < remaining) first++;
            if(total > remaining) last--;
        }
            
    }
    return result;
};