# @param {Integer[][]} cars
# @return {Float[]}
def get_collision_times(cars)
    @cars = cars
    n = cars.length
    
    def speed(idx)
        @cars[idx][1]
    end
    
    def pos(idx)
        @cars[idx][0]
    end
    
    stack = [n-1]
    result = Array.new(n).fill(-1.0)

    
    (n-2).downto(0).each do |idx|
		if speed(idx) <= speed(stack[0])
			stack = [idx]
			next
		end

        while stack.length > 1
            if speed(idx) <= speed(stack[-1]) or ((pos(stack[-1]) - pos(idx)) / Float(speed(idx) - speed(stack[-1]))) >= result[stack[-1]]
                stack.pop
            else
                break
            end
        end

        result[idx] = (pos(stack[-1]) - pos(idx)) / Float(speed(idx) - speed(stack[-1]))
        stack.push(idx)
    end
    result
end
        