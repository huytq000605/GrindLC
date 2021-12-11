# @param {Integer[]} nums
# @return {Integer}
def maximum_gap(nums)
    n = nums.length
    if n < 2
        return 0
    end
    
    min_num = nums.min
    max_num = nums.max
    if max_num == min_num
        return 0
    end
    
    each_bucket = ((max_num - min_num) / Float(n-1)).ceil
    min_buckets = Array.new(n).fill(1<<31)
    max_buckets = Array.new(n).fill(-1)
    
    
    nums.each do |num|
        idx = ((num - min_num) / each_bucket).floor
        min_buckets[idx] = [min_buckets[idx], num].min
        max_buckets[idx] = [max_buckets[idx], num].max
    end

    prev = -1
    result = 0
    for i in 0...n
        if max_buckets[i] == -1
            next
        end
        if prev != -1
            result = [result, min_buckets[i] - prev].max
        end
        prev = max_buckets[i]
    end
    result
end