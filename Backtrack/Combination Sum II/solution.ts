function combinationSum2(candidates: number[], target: number): number[][] {
    let result = []
    candidates.sort((a,b) => a-b) // We sort the candidates first
    helper(candidates, target, 0, [], result)
    return result
};

function helper(nums: number[], target: number, index: number, current: number[], result: number[][]) {
    if (target === 0) {
        result.push([...current]);
        return;
    }

    if (index === nums.length || target < 0) {
        return;
    }

    // We use this index of nums
	current.push(nums[index])
    helper(
        nums,
        target - nums[index],
        index + 1,
		current,
        result
    );
	current.pop()

    let nextIdx = index + 1; // We pass all numbers = nums[index]
    while (nums[nextIdx] === nums[index]) {
        nextIdx++;
    }

    helper(nums, target, nextIdx, current, result);
}