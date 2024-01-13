from operator import iadd


def InsertionSort(array, start, end, sorting_type):
    if sorting_type == "Ascending":
        for i in range(start, end):
            j = i
            while array[j] < array[j - 1] and j > 0:
                array[j], array[j - 1] = array[j - 1], array[j]
                j = j - 1
    if sorting_type == "Descending":
        for i in range(start, end):
            j = i
            while array[j] > array[j - 1] and j > 0:
                array[j], array[j - 1] = array[j - 1], array[j]
                j = j - 1
    return array


def SelectionSort(array, sorting_type):
    if sorting_type == "Descending":
        for i in range(len(array)):
            miniIndex = i
            for j in range(i + 1, len(array)):
                if array[j] > array[miniIndex]:
                    miniIndex = j
            array[i], array[miniIndex] = array[miniIndex], array[i]
    if sorting_type == "Ascending":
        for i in range(len(array)):
            miniIndex = i
            for j in range(i + 1, len(array)):
                if array[j] < array[miniIndex]:
                    miniIndex = j
            array[i], array[miniIndex] = array[miniIndex], array[i]
    return array


def merge_Sort(A, start, end, sorting_type):
    if end > start:
        mid = (start + end) // 2

        merge_Sort(A, start, mid, sorting_type)
        merge_Sort(A, mid + 1, end, sorting_type)

        Merge(A, start, mid, end)
    if sorting_type == "Ascending":
        A = A[::-1]
    return A


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + 1 + j])

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    if i == len(L):
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1
    else:
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1


def BubbleSort(array, sorting_type):
    if sorting_type == "Ascending":
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    if sorting_type == "Descending":
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - 1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array

def quick_sort(arr, order):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x < pivot if order == "Ascending" else x > pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if (x > pivot if order == "Ascending" else x < pivot)]

    if order == "Ascending":
        return quick_sort(left, order) + middle + quick_sort(right, order)
    else:
        return quick_sort(right, order) + middle + quick_sort(left, order)

def Max_Heapify(array, n, i):
    # n is size of heap, i is the root parent
    largest = i
    left_child = (2 * i) + 1
    right_child = (2 * i)
    if left_child < n and array[left_child] > array[largest]:
        largest = left_child
    if right_child < n and array[right_child] > array[largest]:
        largest = right_child
    if largest != i:  # agar left or right ne larget value update kardi
        array[largest], array[i] = array[i], array[largest]
        Max_Heapify(array, n, largest)


def HeapSort(array, n, sorting_type):
    # build max heap
    for i in range((n // 2 - 1), -1, -1):
        # to start from max parent last root to end
        Max_Heapify(array, n, i)
    # deleting element
    for i in range(n - 1, 0, -1):

        array[i], array[0] = array[0], array[i]
        Max_Heapify(array, i, 0)
    if sorting_type == "Descending":
        array = array[::-1]
    return array

def CountingSort(A, sorting_type):
    Max_Element = max(A)
    countArray_len = Max_Element + 1
    countArray = [0] * countArray_len
    Result = [0] * len(A)
    for i in A:
        countArray[i] = countArray[i] + 1

    for i in range(1, Max_Element + 1):
        countArray[i] = countArray[i] + countArray[i - 1]

    i = len(A) - 1
    while i >= 0:
        Result[countArray[A[i]] - 1] = A[i]
        countArray[A[i]] = countArray[A[i]] - 1
        i -= 1
    if sorting_type == "Descending":
        Result = Result[::-1]
    return Result

def counting_sort(arr, order):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)


    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)


    for num in arr:
        count[num - min_val] += 1


    if order == "Descending":
        count = count[::-1]


    for i in range(len(arr)):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output


def RadixCountingSort(A, n):
    Max_Element = max(A)
    countArray_len = Max_Element + 1
    countArray = [0] * countArray_len
    Result = [0] * len(A)
    for i in A:
        temp = i // n
        countArray[temp % 10] += 1

    for i in range(1, Max_Element + 1):
        countArray[i] = countArray[i] + countArray[i - 1]

    i = len(A) - 1
    while i >= 0:
        temp = A[i] // n
        Result[countArray[temp % 10] - 1] = A[i]
        countArray[temp % 10] -= 1
        i -= 1
    return Result


def RadixSort(A, sorting_type):
    Max_Element = max(A)
    d = 1
    while int(Max_Element / d) > 0:
        A = RadixCountingSort(A, d)
        d = d * 10
    if sorting_type == "Descending":
        A = A[::-1]
    return A


#
# def BucketSort(array, sorting_type):
#     if not array:
#         return array
#
#     B = [[] for _ in range(len(array))]
#
#     for j in array:
#         number = int(j * len(array))
#         B[number].append(j)
#
#     for k in range(len(array)):
#         B[k] = sorted(B[k])
#
#     result = [elem for sublist in B for elem in sublist]
#
#     if sorting_type == "Descending":
#         result = result[::-1]
#
#     return result
def bucket_soort(arr, order):
    print("Enter bucket sort")
    arr=arr[0:5]
    print(arr)
    #if not arr:
    #    return arr

    # Find the minimum and maximum values in the input array
    min_val = min(arr)
    print("min",min_val)
    print(type(float(min_val)))
    #print(int(min_val))
    max_val1 = [float(ele) for ele in arr]
    max_val = max(max_val1)
    print(type(max_val))
    print("max",max_val, type(int(max_val)))

    # Determine the range of values
    range_val = float(max_val) - float(min_val)
    range_val=round(range_val,2)
    print("range value",range_val)

    # Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    print("buckerts", buckets)

    # Distribute elements into buckets
    for num in arr:
        print("num", num)
        # Determine which bucket to place the element in
        index = int((float(num) - min_val) // range_val * (num_buckets - 1))
        print("index",index)
        buckets[index].append(num)

    # Sort elements within each bucket using insertion sort
    for i in range(len(buckets)):
        print("Insertion sort")
        insertion_sort(buckets[i], order)

    # Concatenate the sorted buckets to get the final sorted array
    sorted_array = [num for bucket in buckets for num in bucket]

    return sorted_array

def insertion_sort(arr, order):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (key < arr[j] if order == "Ascending" else key > arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def Combsort(A, sorting_type):
    gap = len(A)
    swap = True
    temp = 0
    while gap != 1 or swap == True:
        swap = False
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        for i in range(0, len(A) - gap):
            if A[i] > A[i + gap]:
                temp = A[i]
                A[i] = A[i + gap]
                A[i + gap] = temp
                swap = True
    if sorting_type == "Descending":
        A = A[::-1]
    return A


def ShellSort(A, sorting_type):  # It is actully insertion sort with some optimization and less no of comparisons
    n = len(A)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
    if sorting_type == "Descending":
        A = A[::-1]
    return A


def CocktailSort(A, sorting_type):
    low = 0
    high = len(A) - 1
    while low < high:
        for k in range(low, high):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]
        for i in range(high, low, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
        low += 1
        high -= 1
    if (sorting_type == "Descending"):
        A = A[::-1]
    return A
def PancakeSort(arr, order):
    ascending = order == "Ascending"

    def find_max_index(arr, n):
        max_index = 0
        for i in range(n):
            if (ascending and arr[i] > arr[max_index]) or (not ascending and arr[i] < arr[max_index]):
                max_index = i
        return max_index

    n = len(arr)
    for cur_size in range(n, 1, -1):
        max_index = find_max_index(arr, cur_size)
        if max_index != cur_size - 1:
            if max_index != 0:
                arr = flip(arr, max_index + 1)
            arr = flip(arr, cur_size)

    return arr
def flip(arr, k):
    return arr[:k][::-1] + arr[k:]

def IndexSort(array, sorting_type):
    n = len(array)
    indices = list(range(n))

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (sorting_type == "Ascending" and array[indices[i]] > array[indices[j]]) or (sorting_type == "Descending" and array[indices[i]] < array[indices[j]]):
                indices[i], indices[j] = indices[j], indices[i]

    sorted_arr = [array[i] for i in indices]
    return sorted_arr


