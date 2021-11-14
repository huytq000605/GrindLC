class CombinationIterator {
    result
    idx
    constructor(characters: string, combinationLength: number) {
        this.result = [];
		let dfs = (idx, current) => {
			if(current.length === combinationLength) {
				this.result.push(current)
				return
			}
			for(let i = idx; i < characters.length; i++) {
				dfs(i + 1, current + characters[i])
			}
		}
		dfs(0, "")
        this.idx = 0
    }

    next(): string {
        let res = this.result[this.idx];
        this.idx++
        return res
    }

    hasNext(): boolean {
        return this.idx < this.result.length
    }

}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = new CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */