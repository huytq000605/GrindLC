class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        final_result = math.inf
        minutes = targetSeconds // 60
        seconds = targetSeconds - minutes * 60
        
        if minutes < 100:
            result = 0
            s_right = seconds % 10
            s_left = seconds // 10
            m_right = minutes % 10
            m_left = minutes // 10
            
            current = startAt
            
            if m_left != 0:
                if current != m_left:
                    current = m_left
                    result += moveCost
                result += pushCost

            if m_left != 0 or m_right != 0:
                if current != m_right:
                    current = m_right
                    result += moveCost
                result += pushCost

            if m_left != 0 or m_right != 0 or s_left != 0:
                if current != s_left:
                    current = s_left
                    result += moveCost
                result += pushCost

            if current != s_right:
                current = s_right
                result += moveCost
            result += pushCost
            final_result = result
        
        # CASE 2
        if seconds + 60 <= 99 and minutes >= 1:
            seconds += 60
            minutes -= 1
            result = 0
            s_right = seconds % 10
            s_left = seconds // 10
            m_right = minutes % 10
            m_left = minutes // 10

            current = startAt
            
            if m_left != 0:
                if current != m_left:
                    current = m_left
                    result += moveCost
                result += pushCost

            if m_left != 0 or m_right != 0:
                if current != m_right:
                    current = m_right
                    result += moveCost
                result += pushCost

            if m_left != 0 or m_right != 0 or s_left != 0:
                if current != s_left:
                    current = s_left
                    result += moveCost
                result += pushCost

            if current != s_right:
                current = s_right
                result += moveCost
            result += pushCost
            
            final_result = min(final_result, result)
        return final_result