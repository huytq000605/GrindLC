class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int leftPointer = 0;
        int rightPointer = people.length - 1;
        int boats = 0;
        while(leftPointer <= rightPointer) {
            boats++;
            if(leftPointer == rightPointer) {
                return boats;
            }
            if(people[leftPointer] + people[rightPointer] <= limit) {
                leftPointer++;
                rightPointer--;
            } else {
                rightPointer--;
            }    
        }
        return boats;
    }
}