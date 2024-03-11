impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut keys = std::collections::HashMap::<u8, usize>::new();
        for (i, &b) in order.as_bytes().iter().enumerate() {
            keys.insert(b, i);
        }
        let mut result = s.into_bytes();
        result.sort_by(|a, b| keys.get(a).unwrap_or(&(0 as usize)).
            partial_cmp(keys.get(b).unwrap_or(&(0 as usize))).unwrap());
        return std::str::from_utf8(&result).unwrap().to_string()
    }
}
