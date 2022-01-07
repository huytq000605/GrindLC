# Reservoir Sampling

- Resevoir Sampling is a family of randomized algorithms for choosing a simple random sample, without replacement, of k items from a population of unknown size n in a single pass over the items

- Choosing k elements from n elements (We don't know n, big size, cannot fit in memory)

- Algo:
  - Choosing first k elements to put in reservoir
  - Start from k+1, generate a random number m from 0 to current n
  - If m < k => replace reservoir[m] with stream[k+1]

