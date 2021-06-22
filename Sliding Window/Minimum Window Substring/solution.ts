function minWindow(s: string, t: string): string {
    let counter = new Map() // counter letter of t
    for(let i = 0; i < t.length; i++) {
        counter.set(t[i], ( counter.get(t[i]) || 0 ) + 1)
    }

	// start and end position for result
    let resultStart = 0
    let resultEnd = s.length
	
	// start position for window,
	// needSatisfy is number of letter need to be satisfied in window,
	// satisfied is number of letter has been satisfied
    let start = 0
    let needSatisfy = counter.size;
    let satisfied = 0
	
    for(let end = 0; end < s.length; end++) {
        if(counter.has(s[end])) {
            counter.set(s[end], counter.get(s[end]) - 1)
            if(counter.get(s[end]) === 0) { // If reach 0 => letter has been satisfied
                satisfied++
            }
        }
        
		while(satisfied === needSatisfy) {
			if(end - start < resultEnd - resultStart) { // Get minimum result
				resultStart = start
				resultEnd = end
			}

			if(counter.has(s[start])) {
				if(counter.get(s[start]) === 0) break; // We dont wanna break the satisfy letter
				counter.set(s[start], counter.get(s[start]) + 1)
			}
			start++
		}
		
		
	}
        
    if(resultEnd === s.length) return "" // No result found
    return s.slice(resultStart, resultEnd + 1)
};