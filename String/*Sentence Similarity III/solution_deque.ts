function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    let sen1 = sentence1.split(" ")
    let sen2 = sentence2.split(" ")
    
    let deque1 = []
    let deque2 = []
    
    for(let word of sen1) {
        deque1.push(word)
    }
    
    for(let word of sen2) {
        deque2.push(word)
    }
    
    while(deque1.length && deque2.length && deque1[0] === deque2[0]) {
        deque1.shift()
        deque2.shift()
    }
    
    while(deque1.length && deque2.length && deque1[deque1.length - 1] === deque2[deque2.length - 1]) {
        deque1.pop()
        deque2.pop()
    }
    
    if(deque1.length === 0 || deque2.length === 0) return true
    return false
};