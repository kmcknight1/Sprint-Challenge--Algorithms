#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This code has a loop, running while a is less than n _ n _ n. It sets variable a to itself plus n \* n. This has a runtime complexity of O(n), because it will take n number of loops for this to complete. You can test this by placing any number in for n.

b) This code has a nested loop (loop within a loop). The outer loop is linearly related to the size of n (O(n)) and the inner loop is scaling twice as fast toward n each pass (O(log n)). This gives it a runtime complexity of O(n log n).

c) This code utilizes recursion, running (bunnies - 1), therefore it runs one time per n. This is a runtime complexity of O(n).

## Exercise II

floors = list
f = int
highest floor = high value
lowest floor = low value

Drop an egg at the midpoint, determine if f is higher or lower(if it breaks, f is lower, if not f is higher). If higher, move the low value up. If lower, move the high value down. Repeat until you find f.

This is a binary search and has a runtime complexity of O(log n).
