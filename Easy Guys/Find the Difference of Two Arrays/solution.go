func findDifference(nums1 []int, nums2 []int) [][]int {
    s1, s2 := make(map[int]struct{}), make(map[int]struct{})
    for _, num1 := range nums1 {
        s1[num1] = struct{}{}
    }
    for _, num2 := range nums2 {
        s2[num2] = struct{}{}
    }
    result := [][]int{[]int{}, []int{}}
    for _, num1 := range nums1 {
        if _, ok := s2[num1]; !ok {
            s2[num1] = struct{}{}
            result[0] = append(result[0], num1)
        }
    }
    for _, num2 := range nums2 {
        if _, ok := s1[num2]; !ok {
            s1[num2] = struct{}{}
            result[1] = append(result[1], num2)
        }
    }
    return result
}
