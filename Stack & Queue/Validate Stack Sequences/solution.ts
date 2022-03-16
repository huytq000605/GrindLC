function validateStackSequences(pushed: number[], popped: number[]): boolean {
	if(!pushed.length && !popped.length) return true;
	let stack = [];
	let poppedIndex = 0;
	while(pushed.length) {
			if(stack[stack.length - 1] === popped[poppedIndex]) {
					stack.pop();
					poppedIndex++;
			}
			else stack.push(pushed.shift());
	}
	while(stack.length) {
			if(stack[stack.length - 1] === popped[poppedIndex]) {
					stack.pop();
					poppedIndex++;
					continue;
			}
			else break;
	}
	if(poppedIndex === popped.length) return true;
	return false;
};