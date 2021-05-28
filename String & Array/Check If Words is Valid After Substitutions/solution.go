package main

func isValid(s string) bool {
    stack := make([]byte, 0)
    for i := 0; i < len(s); i++ {
        stack = append(stack, s[i])
        if(s[i] == 99) {
            if len(stack) < 3 {
                return false
            }
            if string(stack[len(stack)-3:]) != "abc" {
                return false
            }
            stack = stack[0:len(stack)-3]
        }
    }
    return len(stack) == 0
}