type V struct {
    Value string
    Time int
}

type TimeMap struct {
    M map[string][]V
}


func Constructor() TimeMap {
    return TimeMap{
        M: make(map[string][]V),
    }
}


func (t *TimeMap) Set(key string, value string, timestamp int)  {
    if _, ok := t.M[key]; !ok {
        t.M[key] = make([]V, 0)
    }
    t.M[key] = append(t.M[key], V{value, timestamp})
}


func (t *TimeMap) Get(key string, timestamp int) string {
    if _, ok := t.M[key]; !ok {
        return ""
    }
    vs := t.M[key]
    start, end := 0, len(vs) - 1
    for start < end {
        mid := start + int(math.Ceil(float64((end - start + 1) / 2)))
        if vs[mid].Time > timestamp {
            end = mid - 1
        } else {
            start = mid
        }
    }
    if vs[start].Time <= timestamp {
        return vs[start].Value
    }
    return ""
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
