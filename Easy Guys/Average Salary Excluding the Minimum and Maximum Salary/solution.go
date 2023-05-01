func average(salary []int) float64 {
    n := len(salary)
    var s int
    mn, mx := salary[0], salary[0]
    for _, sal := range salary {
        s += sal
        if sal < mn {
            mn = sal
        }
        if sal > mx {
            mx = sal
        }
    }
    result := float64(s - mn - mx) / float64(n-2)
    return result
}
