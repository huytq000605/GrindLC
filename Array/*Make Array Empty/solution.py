class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        idxs = {nums[i]:i for i in range(n)}
        nums.sort()
        result = n
        #         This solution is just pure genius!
        # For those who don't understand why res is initialized to n at the beggining, and why res += n-i in the for loop, here's my explanation:

        # So the intuition behind this algorithm is to split the process of removing smallest elements into multiple passes. What does that mean?
        # For better explanation, I'll use an example [1,4,5,2,8,7,6,3], where n=size of array=8
        # We split the process of removing smallest elements into 4 passes:
        # remove [1,2,3]
        # remove [4,5,6]
        # remove [7]
        # remove [8]

        # OK, so this is where the magic happens, to remove [1,2,3] from the array, we need to remove 1, move 4 to the back, move 5 to the back, remove 2, move 8 to the back, move 7 to the back, move 6 to the back, remove 3. The first pass uses n=size of array=8 operations, regardless what elements are in the first pass. This is why we initialize res to n.

        # Now, the remaining of the array is [4,5,8,7,6] after removing [1,2,3]
        # We want to remove [4,5,6] from the remaining array, we need to remove 4, remove 5, move 8 to the back, move 7 to the back, remove 6. And this pass takes 5 operations, which is equal to the size of the remaining array. This is why res += n - i. (since n - i is the size of the remaining array)

        # The remaining array is now [8,7]
        # And its the same process for the third pass of removing [7], move 8 to the back, remove 7, wihch takes 2 operaions, which is equal to the remaining size of the array

        # The remaining array is now [8]
        # Lastly, we just remove 8, which takes 1 operation

        # Now, how do we split this process into passes in code?
        # Since the array has been sorted, ex: [1,2,3,4,5,6,7,8], and we know the index of each element using hashmap, if we encounter a number with smaller index than previous number, we can split out a pass.
        for i in range(n-1):
            if idxs[nums[i+1]] < idxs[nums[i]]:
                result += n - i - 1
        return result
            
