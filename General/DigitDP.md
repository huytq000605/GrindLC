# Digit Dynamic Programming

## Typical problem will ask finding how many numbers with some conditions are there between [low, high]

We cannot just simply backtrack the number because low and high can be up to 10^18 or even more

Idea: Have a function which find all the valid numbers below than a value and have some states

## func dp(i, mx, tight, leading_zero)
### i start from 0
### mx is the maximum value
### tight indicates that all the previous degits still equal to mx
### leading_zero means that at this position, is that all the previous digits are 0 





