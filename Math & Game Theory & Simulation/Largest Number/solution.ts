function largestNumber(nums: number[]): string {
    let str = nums.map((e) => `${e}`)
    quicksort(str, 0, str.length - 1, function(a,b) {
        let cmp1 = a + b
        let cmp2 = b + a
        if(cmp1 > cmp2) return -1
        if(cmp1 === cmp2) return 0
        return 1
    })
    if(str[0] === "0") return "0"
    return str.join("")
};

function quicksort(arr, start, end, cmpFn) {
    if(start >= end) return    
    let i = 0, j = start-1;
    let pivot = end
    for(let i = start; i < end; i++) {
        if(cmpFn(arr[i], arr[pivot]) === -1) {
            j++
            [arr[i], arr[j]] = [arr[j], arr[i]]
        }
    }
    j++
    [arr[j], arr[pivot]] = [arr[pivot], arr[j]]
    quicksort(arr, start, j - 1, cmpFn)
    quicksort(arr, j + 1, end, cmpFn)
}
