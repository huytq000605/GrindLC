# @param {Integer[][]} triplets
# @param {Integer[]} target
# @return {Boolean}
def merge_triplets(triplets, target)
    a,b,c = 0,0,0
    triplets.each do |triplet|
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]
            next
        end
        a = [a, triplet[0]].max
        b = [b, triplet[1]].max
        c = [c, triplet[2]].max
    end
    
    if a != target[0] or b != target[1] or c != target[2]
        return false
    end
    
    return true
end