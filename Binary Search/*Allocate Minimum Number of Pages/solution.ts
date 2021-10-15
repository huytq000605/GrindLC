function allocate(pages: number[], students: number): number {
	if(pages.length < students) return -1
	let sum = 0
	let min = Number.MAX_SAFE_INTEGER
	for(let page of pages) {
		sum += page
		min = Math.min(min, page)
	}
	let max = sum
	while(min < max) {
		let maxEach = min + Math.floor((max - min) / 2)
		if(isPossible(pages, maxEach, students)) {
			max = maxEach
		} else {
			min = maxEach + 1
		}
	}
	return min
}

function isPossible(pages: number[], maxEach: number, students: number) {
	let currentSum = 0
	let currentStudent = 1
	for(let page of pages) {
		if(currentSum + page > maxEach) {
			currentStudent++
			if(currentStudent > students) return false
			currentSum = page
		} else {
			currentSum += page
		}
	}
	return true
}