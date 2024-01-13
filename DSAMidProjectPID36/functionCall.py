from SortingAlgorithm import bucket_soort,insertion_sort,counting_sort
import SortingAlgorithm
import time
import ParseData

def SortingAlgorithmFunction_Call(A, sorttype, sortalgo):
    original = A.copy()
    res = []
    startTime = time.time()

    if (sortalgo == "InsertionSort"):
        res = SortingAlgorithm.InsertionSort(A, 0, len(A), sorttype)

    elif (sortalgo == "SelectionSort"):
        res = SortingAlgorithm.SelectionSort(A, sorttype)

    elif (sortalgo == "MergeSort"):
        res = SortingAlgorithm.merge_Sort(A, 0, len(A) - 1, sorttype)

    elif (sortalgo == "BubbleSort"):
        res = SortingAlgorithm.BubbleSort(A, sorttype)

    elif (sortalgo == "QuickSort"):
        res = SortingAlgorithm.quick_sort(A,  sorttype)

    elif (sortalgo == "HeapSort"):
        res = SortingAlgorithm.HeapSort(A, len(A), sorttype)

    elif (sortalgo == "CountingSort"):
        res = SortingAlgorithm.counting_sort(A, sorttype)

    elif (sortalgo == "RadixSort"):
        res = SortingAlgorithm.RadixSort(A, sorttype)


    elif (sortalgo == "BucketSort"):
        print("Enter...")
        res = SortingAlgorithm.bucket_soort(A,sorttype)

    elif (sortalgo == "CombSort"):
        res = SortingAlgorithm.Combsort(A, sorttype)

    elif (sortalgo == "ShellSort"):
        res = SortingAlgorithm.ShellSort(A, sorttype)

    elif (sortalgo == "CockailSort"):
        res = SortingAlgorithm.CocktailSort(A, sorttype)

    elif (sortalgo == "IndexSort"):
        res = SortingAlgorithm.IndexSort(A, sorttype)

    elif (sortalgo == "PancakeSort"):
        res = SortingAlgorithm.PancakeSort(A, sorttype)


    # indexes = DataFilter.SortingAlgorithmIndexes(original, res)
    endTime=time.time()
    totalTime=endTime-startTime
    return res,totalTime