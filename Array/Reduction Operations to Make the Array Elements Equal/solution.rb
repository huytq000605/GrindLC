# @param {Integer[]} nums
# @return {Integer}
def reduction_operations(nums)
    nums = nums.sort_by {|num| -num}
    numOfNumber = 0
    result = 0
    for i in (0...nums.length)
        if i > 0 and nums[i] != nums[i-1]
            result += numOfNumber
        end
        numOfNumber += 1
    end
    
    return result
end