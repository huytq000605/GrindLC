function longestCommonSubsequence(text1: string, text2: string): number {
    let map = new Map()
	let result = helper(text1, text2, 0, 0, map);
	return result
}

function helper(str1: string, str2: string, start1: number, start2: number, map: Map<any,any>): number {
	let key = `${start1}-${start2}`
	if(map.has(key)) {
		return map.get(key)
	}

	if (start1 === str1.length || start2 === str2.length) {
		return 0
	}

	if(str1[start1] == str2[start2]) {
		map.set(key, helper(str1, str2, start1 + 1, start2 + 1, map))
		return map.get(key)
	} else {
		let res1 = helper(str1, str2, start1 + 1, start2, map); // Continue to check next ele for str1 and the same str2
		let res2 = helper(str1, str2, start1, start2+ 1, map)
		let result = Math.max(res1, res2)
		map.set(key, result)
		return result
	}
}