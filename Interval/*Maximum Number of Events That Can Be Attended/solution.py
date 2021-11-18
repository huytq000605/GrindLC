class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda event: event[0])
        heap = []
        idx = 0
        currentDay = 0
        result = 0
        while idx < len(events) or len(heap):
            # Remove all expired events
            while len(heap) and heap[0] < currentDay:
                heappop(heap)
            # Add all events that can attend
            while idx < len(events) and events[idx][0] <= currentDay:
                heappush(heap, events[idx][1])
                idx += 1
            # Attend an event
            if len(heap):
                result += 1
                heappop(heap)
            # Optimize or move to next day
            if len(heap) == 0 and idx < len(events):
                currentDay = events[idx][0]
            else:
                currentDay += 1
                
        return result