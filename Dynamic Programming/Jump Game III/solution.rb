# @param {Integer[]} arr
# @param {Integer} start
# @return {Boolean}
def can_reach(arr, start)
    stack = [start]
    seen = {}
    while stack.length > 0
        curr = stack.pop
        [curr + arr[curr], curr - arr[curr]].each do |nextPosition|
            if nextPosition < 0 or nextPosition >= arr.length or seen.key? nextPosition
                next
            end
            if arr[nextPosition] == 0
                return true
            end
            seen[nextPosition] = true
            stack.push(nextPosition)
        end
    end
    false
end