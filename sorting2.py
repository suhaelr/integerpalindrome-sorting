# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Verify it works
random_list_of_nums = [10,2,1,5,3,6]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

#The worst case scenario is when the smallest or largest element is always selected as the pivot.
#This would create partitions of size n-1, causing recursive calls n-1 times. This leads us to a worst case time complexity of O(n^2).
#While this is a terrible worst case, Quick Sort is heavily used because it's average time complexity is much quicker. 
#While the partition function utilizes nested while loops, it does comparisons on all elements of the array to make its swaps. As such, it has a time complexity of O(n).
#With a good pivot, the Quick Sort function would partition the array into halves which grows logarithmically with n. 
#Therefore the average time complexity of the Quick Sort algorithm is O(nlog(n)).
#Merge sort is more efficient and works faster than quick sort in case of larger array size or datasets. 
#Quick sort is more efficient and works faster than merge sort in case of smaller array size or datasets.

