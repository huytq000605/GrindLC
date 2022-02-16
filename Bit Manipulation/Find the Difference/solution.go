func findTheDifference(s string, t string) byte {
    xor := 0
    for i := 0; i < len(s); i++ {
        xor ^= int(s[i])
        xor ^= int(t[i])
    }
    xor ^= int(t[len(t) - 1])
    return byte(xor)
}
