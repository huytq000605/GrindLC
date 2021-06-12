/*
We do it the reverse way
*/

function deckRevealedIncreasing(deck: number[]): number[] {
    deck.sort((a,b) => a-b);
    let result = []
    helper(deck, result)
    return result
};

function helper(deck: number[], result: number[]) {
    if(deck.length) {
        if(result.length) {
            result.unshift(result.pop())
        }
        result.unshift(deck.pop())
        return helper(deck, result)
    }
}