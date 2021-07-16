// Find sum of current array(1)
// Find sum of original array(2)
// missingNumber = (2) - (1)
function findingMissing(arr: number[]): number {
	// We have sum = num + num + diff + num + 2*diff + ... + num + (n-1) * diff
	// => originalSum = n* num + n*(n-1)/2 * diff
	// max - min = (n-1) * diff
	let min = Number.MAX_SAFE_INTEGER
	let max = Number.MIN_SAFE_INTEGER
	let sum = 0
	for(let num of arr) {
		min = Math.min(min, num)
		max = Math.max(max, num)
		sum += num
	}
	let diff = (max - min) / arr.length
	let n = arr.length + 1
	let originalSum = n * min + n*(n-1)/2 * diff
	let missingNumber = originalSum - sum
	return missingNumber
	
}