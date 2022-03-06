function isSubsequence(s: string, t: string): boolean {
	let idx = 0;
	if(s.length === 0) return true;
	for(let i = 0; i < t.length; i++) {
			if(t[i] === s[idx]) {
					idx++;
					if(idx === s.length) return true;
			}
	}
	return false;
};