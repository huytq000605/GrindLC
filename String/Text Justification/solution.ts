function fullJustify(words: string[], maxWidth: number): string[] {
    let result = []
    let currentLength = 0
    let currentWords = []
    for(let word of words) {
		// We only check if we are currently have some word already
		// When we adding new word, we need to + 1 for space
        if(currentWords.length && currentLength + 1 + word.length > maxWidth) { 
            if(currentWords.length === 1) {
                let appendSpace = maxWidth - currentWords[0].length
                let bePushedWord = currentWords[0]
				bePushedWord += getSpaceString(appendSpace)
                result.push(bePushedWord)
            } else {
                let toBePushed = ""
                let remainingSpace = maxWidth - currentLength // This is how many remaining space we got after we + space for each word
                let eachWordTake = Math.floor(remainingSpace / (currentWords.length - 1)) // Left allign
                let firstPlusOne = remainingSpace % (currentWords.length - 1)
                for(let i = 0; i < currentWords.length - 1; i++) { // Last word doesn't take space
                    if(i < firstPlusOne) {
                        currentWords[i] += getSpaceString(eachWordTake + 1 + 1)
                    } else {
                        currentWords[i] += getSpaceString(eachWordTake + 1)
                    }
                    toBePushed += currentWords[i]
                }
                toBePushed += currentWords[currentWords.length - 1] // push last word
                result.push(toBePushed)
            }
            currentWords = []
            currentLength = 0
        }
        currentWords.push(word)
        if(currentLength > 0) {
            currentLength += word.length + 1 // Push the space
        } else {
            currentLength += word.length // Not need the space cause only 1 word
        }
        
    }
    
	// Push the last and right allign
    let lastPushed = ""
    for(let i = 0; i < currentWords.length; i++) {
        if(i !== currentWords.length - 1) {
            lastPushed += currentWords[i] + " "
        } else {
            lastPushed += currentWords[i]
        }
    }
    lastPushed += getSpaceString(maxWidth - currentLength)
    result.push(lastPushed)
    
    return result
};
                        
                            
function getSpaceString(spaces: number) {
    let str = ""
    for(let i = 0; i < spaces; i++) str += " "
    return str
}