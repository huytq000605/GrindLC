package main

type MagicDictionary struct {
	dict []string
}

/** Initialize your data structure here. */
func Constructor() MagicDictionary {
	return MagicDictionary{}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	this.dict = dictionary
}

func (this *MagicDictionary) Search(searchWord string) bool {
	for _, word := range this.dict {
		if magic(searchWord, word) {
			return true
		}
	}
	return false
}

func magic(src, des string) bool {
	if len(src) != len(des) {
		return false
	}
	flag := false
	for i := 0; i < len(src); i++ {
		if src[i] != des[i] {
			if flag {
				return false
			} else {
				flag = true
			}
		}
	}
	if flag {
		return true
	} else {
		return false
	}
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
 */
