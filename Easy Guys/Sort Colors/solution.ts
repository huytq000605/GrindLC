/**
 Do not return anything, modify nums in-place instead.
 */
 function sortColors(nums: number[]): void {
    quickSort(nums)
};

function quickSort(arr) {
    let partition = (start, end) => {
        if(start >= end) return
        let pivot = arr[end]
        let j = start - 1
        for(let i = start; i <= end; i++) {
            if(arr[i] < pivot) {
                j++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
        j++;
        [arr[j], arr[end]] = [arr[end], arr[j]];
        partition(start, j - 1)
        partition(j + 1, end)
    }
    partition(0, arr.length - 1)
}