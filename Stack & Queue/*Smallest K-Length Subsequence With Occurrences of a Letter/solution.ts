function smallestSubsequence(s: string, k: number, letter: string, repetition: number): string {
    let count = 0
    let have = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === letter) count++
    }
    let stack = []
    for(let i = 0; i < s.length; i++) {
        while(stack.length && s[i] < stack[stack.length - 1] && stack.length - 1 + (s.length - i) >= k) { // If we met a smaller element and we still have enough letter to fill
			if(stack[stack.length - 1] !== letter  || (stack[stack.length - 1] === letter && have + count - 1 >= repetition)) { // If we still have enough repetition letter to fill
				if(stack.pop() === letter) have--
			} else {
				break
			}
		
        }
		if(stack.length < k) { // If the current result length < k
			if(s[i] === letter) { // Increase the have
                stack.push(letter)
                have++
            }
			else if(k - stack.length > repetition - have) stack.push(s[i]) // We must left space for repetition letter if it hasn't met requirement
		}
        if(s[i] === letter) count--
        
    }
    return stack.join("")
};