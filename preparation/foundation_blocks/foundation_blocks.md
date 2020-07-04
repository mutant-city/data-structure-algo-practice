### Partitioning

* splitting an array into two parts based on a condition

* 'multi data structure'
    * two lists and iterate through and assign to either list based on a condition
    * then join the lists
    * O(n) but has added space complexity

* 'in place'
    * O(n) but removes the space complexity
    * Have two array pointers, on insertion index and one test index
        * traverse every array item with the test index and test it's partition state
            * if it meets partition state for being on the left
                * swap test index and insertion index
                * increment insertion index.
* References                
    * http://p-nand-q.com/python/algorithms/sorting/partitioning.html



### Swapping
* Store one value in tmp variable
* other lang specific ways but this is portable
'''
    tmp = in_array[j]
    in_array[j] = in_array[k]
    in_array[k] = tmp
'''

### Shifting 
* Shift all values up
    * use swap and iterate backwards





