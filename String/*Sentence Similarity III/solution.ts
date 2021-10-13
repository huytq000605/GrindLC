function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    let sen1 = sentence1.split(" ")
    let sen2 = sentence2.split(" ")
    
    let shorter
    let longer
    if(sen1.length < sen2.length) {
        shorter = sen1
        longer = sen2
    } else {
        shorter = sen2
        longer = sen1
    }
    
    let prefix = -1
    for(let i = 0; i < shorter.length; i++) {
        if(shorter[i] === longer[i]) {
            prefix = i
        } else {
            break
        }
    }
    
    let suffix = shorter.length
    let right = longer.length - 1
    for(let i = shorter.length - 1; i > prefix; i--, right--) {
        if(shorter[i] === longer[right]) {
            suffix = i
        } else {
            break
        }
    }
    
    if(prefix + 1 === suffix) {
        return true
    }
    return false
};