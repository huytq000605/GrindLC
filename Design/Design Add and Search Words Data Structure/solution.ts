class WordDictionary {
    trie
    constructor() {
        this.trie = {}
    }

    addWord(word: string): void {
        let current = this.trie
        for(let letter of word) {
            if(!current[letter]) {
                current[letter] = {}
            }
            current = current[letter]
        }
        current.isWord = true
    }

    search(word: string): boolean {
        return this.privateSearch(word, 0, this.trie)
    }

    privateSearch(word, index, current) {
        if(index === word.length) {
            if(current.isWord)
                return true
            else return false
        }
        let letter = word[index]
        if(letter === ".") {
            for(let key of Object.keys(current)) {
                if(key === "isWord") continue
                if(this.privateSearch(word, index + 1, current[key])) return true
            }
            return false
        } else {
            if(!current[letter]) {
                return false
            }
            return this.privateSearch(word, index + 1, current[letter])
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */