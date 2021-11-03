# @param {String} s
# @param {String} part
# @return {String}
def remove_occurrences(s, part)
    @stack = []
    @part = part
    def check()
        i = @stack.length - 1
        j = @part.length - 1
        while i >= 0 && j >= 0 && @stack[i] == @part[j]
            i -= 1
            j -= 1
        end
        return j == -1
    end
    
    (0...s.length).each do |i|
        @stack.push(s[i])
        while @stack.length >= part.length && check
            (0...part.length).each do |j|
                @stack.pop()
            end
        end
    end
    
    @stack.join("")
end