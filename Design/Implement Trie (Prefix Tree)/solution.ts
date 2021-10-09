class Trie {
    trie
    constructor() {
        this.trie = {}
    }

    insert(word: string): void {
        let current = this.trie
        for(let i = 0; i < word.length; i++) {
            if(!current[word[i]]) {
                current[word[i]] = {}
            }
            current = current[word[i]]
        }
        current.isWord = true
    }

    search(word: string): boolean {
        let current = this.trie
        for(let i = 0; i < word.length; i++) {
            if(!current[word[i]]) return false
            current = current[word[i]]
        }
        if(!current.isWord) return false
        return true
    }

    startsWith(prefix: string): boolean {
        let current = this.trie
        for(let i = 0 ; i < prefix.length; i++) {
            if(!current[prefix[i]]) return false
            current = current[prefix[i]]
        }
        return true
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */