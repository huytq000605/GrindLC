# @param {Integer} n
# @param {Integer[][]} edge_list
# @param {Integer[][]} queries
# @return {Boolean[]}
class UnionFind
    def initialize(n)
        @p = Array.new(n).map!.with_index {|ele, idx| idx}
        @r = Array.new(n).fill(1)
    end
    
    def find(x)
        if x != @p[x]
            @p[x] = find(@p[x])
        end
        @p[x]
    end
    
    def union(x, y)
        x_p, y_p = find(x), find(y)
        if x_p == y_p
            return
        end
        
        if @r[x_p] < @r[y_p]
            x_p, y_p = y_p, x_p
        end
        
        @r[x_p] += @r[y_p]
        @p[y_p] = x_p
    end
        
end

def distance_limited_paths_exist(n, edge_list, queries)
    edge_list.sort! {|a,b| a[2] - b[2]}
    queries.map!.with_index {|query, idx| [*query, idx]}.sort! {|a,b| a[2] - b[2]}
    uf = UnionFind.new(n)
    result = Array.new(queries.length)
    idx = 0
    queries.each do |query|
        u, v, limit, i = query
        while idx < edge_list.length && edge_list[idx][2] < limit
            uf.union(edge_list[idx][0], edge_list[idx][1])
            idx += 1
        end
        if uf.find(u) != uf.find(v)
            result[i] = false
        else
            result[i] = true
        end
    end
    result
        
end
