impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let mut track = std::collections::HashMap::<i32, Vec<i32>>::new();
        for (i, group) in group_sizes.iter().enumerate() {
            track.entry(*group).
                and_modify(|e| { (*e).push(i as i32) }).
                or_insert(vec![i as i32]);
            if track.get(group).unwrap().len() == *group as usize {
                result.push(track.remove(group).unwrap());
            }
        }
        return result
    }
}
