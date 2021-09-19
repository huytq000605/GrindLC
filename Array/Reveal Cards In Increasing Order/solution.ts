function deckRevealedIncreasing(deck: number[]): number[] {
    deck.sort((a,b) => a-b)
    let result = []
    while(deck.length) {
        if(result.length) result.unshift(result.pop())
        result.unshift(deck.pop())
    }
    return result
};