# @param {Integer[]} nums
# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def num_subarray_bounded_max(nums, left, right)
    @nums = nums
    def count(k)
        result = 0
        start = 0
        for i in (0...@nums.length)
            if @nums[i] > k
                start = i + 1
                next
            end
            
            result += i - start + 1
        end
        result
    end
    
    count(right) - count(left - 1)
end