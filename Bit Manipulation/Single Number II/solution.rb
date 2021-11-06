# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    @arr = Array.new(32).fill(0)
    
    def addNum(num)
        for i in (0...32)
            if num & (1 << i) != 0
                @arr[i] += 1
            end
        end
    end
    
    nums.each do |num|
        addNum(num)
    end
    
    result = 0
    negative = false
    
    for i in (0...32)
        if @arr[i] % 3 != 0
            result |= (1 << i)
            if i == 31
                negative = true
            end
        end
    end
        
    if negative
        result = -(2 ** 32 - result)
    end
        
    result
end