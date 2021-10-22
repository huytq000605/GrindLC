class WordFilter {
    prefixTrie: Record<any, any>
    suffixTrie: Record<any, any>
    words: string[]
    constructor(words: string[]) {
        this.prefixTrie = {}
        this.suffixTrie = {}
        for(let i = 0; i < words.length; i++) {
            this.addToTrie(this.prefixTrie, words[i], i)
            this.addToSuffixTrie(this.suffixTrie, words[i], i)
        }
        this.words = words
    }

    f(prefix: string, suffix: string): number {
        let result = -1
        let set = new Set()
        let putWordIntoSet = (trie) => {
            for(let key of Object.keys(trie)) {
                if(key === "word") {
                    set.add(trie[key])
                } else {
                    putWordIntoSet(trie[key])
                }
            }
        }
        
        let getWordFromSet = (trie) => {
            for(let key of Object.keys(trie)) {
                if(key === "word") {
                    if(set.has(trie[key])) result = Math.max(result, trie[key])
                } else {
                    getWordFromSet(trie[key])
                }
            }
        }
        
        
        let current = this.prefixTrie
        for(let i = 0; i < prefix.length; i++) {
            if(!current[prefix[i]]) return -1
            current = current[prefix[i]]
        }
        putWordIntoSet(current)
        
        current = this.suffixTrie
        for(let i = suffix.length - 1; i >= 0; i--) {
            if(!current[suffix[i]]) return -1
            current = current[suffix[i]]
        }
        getWordFromSet(current)
        
        return result
        
        
        
    }

    addToTrie(trie: Record<any, any>, str: string, i: number) {
        let current = trie
        for(let i = 0; i < str.length; i++) {
            if(!current[str[i]]) current[str[i]] = {}
            current = current[str[i]]
        }
        current.word = i
    }

    addToSuffixTrie(trie: Record<any, any>, str: string, i: number) {
        for(let i = str.length - 1; i >= 0; i--) {
            if(!trie[str[i]]) trie[str[i]] = {}
            trie = trie[str[i]]
        }
        trie.word = i
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(prefix,suffix)
 */