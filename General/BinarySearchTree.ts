/*
Signal for a problem about binary search tree is that you can get the range minimum to maximum of answer, find a value that fit condition for an array (experience ...)

So when you try to BST, compare the current value you are using to condition, the ">" and "<" is easy to put in, but the "=" is a little tricky to understand.
Example: When the problem asks you for finding min for condition, if the value is fit for the condition, you can keep decrease/increase the max/min to get the real min answer

Example with Find the smallest divisor given a threshold: 
    If sum <= threshold then can keep decrease the max value to find a more smaller divisior that fit the condition
    If sum > threshold then we are sure that the current value we are using is wrong, then just let min = mid + 1


************************** THE FINAL ANSWER SHOULD BE WHEN MIN = MAX *****************************************************
*/