impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let (mut start, mut end) = (1, n-2);
        while start < end {
            let mid = start + (end - start) / 2;
            if arr[mid] < arr[mid+1] {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start as i32
    }
}
