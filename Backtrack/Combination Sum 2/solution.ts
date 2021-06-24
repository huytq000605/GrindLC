function combinationSum2(candidates: number[], target: number): number[][] {
    let result = []
    candidates.sort((a,b) => a-b)
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

	current.push(nums[index])
    helper(
        nums,
        target - nums[index],
        index + 1,
		current,
        result
    );
	current.pop()

    let nextIdx = index + 1;
    while (nums[nextIdx] === nums[index]) {
        nextIdx++;
    }

    helper(nums, target, nextIdx, current, result);
}