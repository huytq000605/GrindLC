## Think different:
- The problem can be translated as: "Given an array, choose arr[i], remove arr[i] with cost = arr[i] * arr[i-1] or cost = arr[i] * arr[i+1], keep doing it until array only have 1 element, return the minimum cost" 
- So what we want to do is find the minimum of the array, remove it with min cost = Math.min(arr[i] * arr[i-1], arr[i] * arr[i+1])
- We can do it by keep finding minimum and remove each element
- Better approach will be using monotonic stack, each time we find a smaller element, we can try to remove it (because we keep doing it until arr.length === 1)