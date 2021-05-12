/*
Another typical example for Monotonous Stack
*/

function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    let greaterElementMap: Map<number, number> = new Map();
    let stack: number[] = [];
    let result = []
    for (let i = 0; i < nums2.length; i++) {
        while (stack.length && nums2[i] > stack[stack.length - 1]) {
            greaterElementMap.set(stack.pop(), nums2[i]);
        }
        stack.push(nums2[i]);
    }
    for(let num of nums1) {
        result.push(greaterElementMap.get(num) || -1)
    }
    return result
}


// Another way but uglier code, from nums1 => nums2
// function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
//     let map = new Map();
//     let stack = [];
//     let result = Array(nums1.length).fill(-1);
//     for (let i = 0; i < nums1.length; i++) {
//         map.set(nums1[i], i);
//     }
//     for (let i = 0; i < nums2.length; i++) {
//         while (stack.length && nums2[stack[stack.length - 1]] < nums2[i]) {
//             let idx = stack.pop();
//             if (map.has(nums2[idx])) result[map.get(nums2[idx])] = nums2[i];
//         }
//         stack.push(i);
//     }
//     return result;
// }
