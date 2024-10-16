// Can use Max_Heap like in python solution
function longestDiverseString(a: number, b: number, c: number): string {
    let map = [{word: 'a', remain: a}, {word: 'b', remain: b}, {word: 'c', remain: c}]
    let result = ""
    while(true) {
        let append = construct(map, result);
        if(append !== "") {
            result += append
        } else { // If nothing to append
            break
        }
    }
    return result
};

function construct(map, current) {
    map.sort((a,b) => b.remain - a.remain) // Sort by the remaining of word can use by desc
    let lastWord = current[current.length - 1] // Get the last word of current result
    if(lastWord == map[0].word) { // If the last word is equal to the highest remaining word => we append the second highest reamining word only 1
        if (map[1].remain > 0) {
            map[1].remain --
            return map[1].word
        } else {
            return ""
        }
        
    }
    if(map[0].remain >= 2) { // Just append the most as i can
        map[0].remain -= 2
        return map[0].word + map[0].word
    } else {
		if(map[0].remain == 0) return "" // Nothing to append
		map[0].remain = 0;
        return map[0].word
	}
}