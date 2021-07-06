## Where to start your thinking
Always keep in mind: interviewers rarely expect you to invent new algorithms. They almost always test your understanding and skills to apply algorithms you've learned at school.

So, what algorithms have you learned at schools that are usually used to solve questions involving an array? DP, search/sort, divide and conquer, greedy.... Hmm... this question reminds me of the question about scheduling meetings with limited meeting rooms, which is solved by greedy algorithm. Even if you don't know the scheduling meeting question, you can swiftly attempt with DP and divide-and-conquer, and will find it is not very straight forward to define the subproblem of DB, or to find the split point of divide-and-conquer. Hmm... so greedy algorithm looks like the right one. Let's try that.

## Greedy algorithm intuition
Greedy algorithms are usually very intuitive (but not necessarily correct. it requires proof). What would you do, if you have multiple equally important meetings to run, but can only make some of them? Most people probably would choose to go to the one that is going to end soon. And after that meeting, pick the next meeting from those that are still available.

## Greedy algorithm proof
At some day, suppose both events **E1** and **E2** are available to choose to attend. For contradictory purpose, suppose the event **E1** that is going to end sooner is not the best choice for now. Instead, **E2** that ends later is the best choice for now. By choosing **E2** now, you come up with a schedule **S1**.

I claim that I can always construct another schedule **S2** in which we choose **E1** instead of **E2** for now, and **S2** is not worse than **S1**.
In **S1**, from now on, if **E1** is picked some time after, then I can always swap **E1** and **E2** in **S1**, so I construct a **S2** which is not worse than **S1**.
In **S1**, from now on, if **E1** is not picked some time after, then I can aways replace **E2** in **S1** with **E1**, so I construct a **S2** which is not worse than **S1**.

So it is always better (at least not worse) to always choose the event that ends sooner.

## Greedy algorithm implementation
As we go through each days to figure out the availability of each events, it is very intuitive to first sort the events by the starting day of the events. Then the question is, how to find out which (still available) event ends the earliest? It seems that we need to sort the currently available events according to the ending day of the events. How to do that? Again, the interviewers don't expect you to invent something realy new! What data structures / algorithm have you learned that can efficiently keep track of the biggest value, while you can dynamically add and remove elements? ...... Yes! Binary search/insert and min/max heap! Obviously, heap is more efficient than binary search, because adding/removing an elements after doing binary search can potentionally cause linear time complexity.

<hr>

## Which one shall we attend?
Intuitively, the one that ends earliest.

## How shall we select an event that ends earliest among a set of attendable events?
Maintain a min heap, where events inside at day t are attendable.

## What are attendable events?
start <= t <= end and not attended yet

To achieve start <= t <= end, we can add an event to the min heap when we are at day start; and remove events with end < t at day t before selecting an event to attend.

To achieve not attended yet, we might sort events by start time, and maintain pointer eventId, where events before eventId are either attended or not attendable.


``` java
class Solution {
    public int maxEvents(int[][] events) {
        // Maintains ends of attendable events at day t:
        //  - start <= t <= end
        //  - not attended yet
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        Arrays.sort(events, (a, b) -> (a[0] == b[0])? a[1] - b[1] : a[0] - b[0]);
        
        int min = Integer.MAX_VALUE, max = 1;
        for (int[] event : events) {
            min = Math.min(min, event[0]);
            max = Math.max(max, event[1]);
        }
        
        int t = min, eventId = 0, cntMaxEvents = 0;
        while (t <= max) {
            if (minHeap.isEmpty()) {
                // No attendable events
                if (eventId < events.length)
                    t = events[eventId][0];
                else
                    break;
            }
            
            // Construct attendable events min heap
            while (eventId < events.length 
                   && events[eventId][0] <= t) {
                minHeap.offer(events[eventId][1]);
                eventId++;
            }
            while (!minHeap.isEmpty()
                   && minHeap.peek() < t) {
                minHeap.poll();
            }
            
            if (!minHeap.isEmpty()) {
                // Attends the one ends earliest
                minHeap.poll();
                cntMaxEvents++;
            }
            
            t++;
        }
        
        return cntMaxEvents;
    }
}
```