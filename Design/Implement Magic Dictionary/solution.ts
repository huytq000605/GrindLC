class MagicDictionary {
    dict: string[]
    constructor() {
        this.dict = []
    }

    buildDict(dictionary: string[]): void {
        this.dict = dictionary;
    }

    search(searchWord: string): boolean {
        for(let word of this.dict) {
            if(this.magic(searchWord, word)) {
                return true
            }
        }
        return false
    }
    
    private magic(str: string, compare: string): boolean {
        if(str.length !== compare.length) return false;
        let flag = false;
        for(let i = 0; i < str.length; i++) {
            if(str[i] !== compare[i]) {
                if(flag) {
                    return false
                } else {
                    flag = true
                }
            }
        }
        if(flag) {
            return true
        } else {
            return false
        }
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */