impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        arr.sort();
        for i in 1..arr.len() {
            if arr[i] - arr[i-1] != arr[1] - arr[0] {
                return false
            }
        }
        true
    }
}
