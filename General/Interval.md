# Interval

## Remove all overlapping interval
Sorted by end, then remove all the overlapping

## Only go the right (#757. Set Intersection Size At Least Two)
intervals.sort(lambda interval: (interval[1], -interval[0]))