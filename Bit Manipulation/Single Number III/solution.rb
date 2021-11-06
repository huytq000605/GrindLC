# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
    aXORb = 0
    nums.each do |num|
        aXORb = aXORb ^ num
    end
    
    rightMostBit = 0
    for position in (0...32)
        if aXORb & (1 << position) != 0
            rightMostBit = position
        end
    end
    
    a = 0
    nums.each do |num|
        if num & (1 << rightMostBit) != 0
            a ^= num
        end
    end
    
    return [a, aXORb ^ a]
end