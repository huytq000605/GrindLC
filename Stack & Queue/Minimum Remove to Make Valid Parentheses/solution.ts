function minRemoveToMakeValid(s: string): string {
	let stack = [];
	let remove = new Set()
	for(let i = 0; i < s.length; i++) {
			if(s[i] === '(') stack.push(i);
			if(s[i] === ')') {
					if(!stack.length) remove.add(i);
					else stack.pop();
			} 
	}
	for(let ele of stack)
			remove.add(ele);
	let result = ""
	for(let i = 0; i < s.length; i++) {
			if(remove.has(i)) continue;
			result += s[i];
	}
	return result;
};