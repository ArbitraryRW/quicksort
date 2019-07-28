print("[+] Basic Quicksort")

def quicksort(arr):
    """
    Base case : 1 item or less left in array
    Recursive case : Recursively invoke quick sort with a subet array

    :param arr:
    :return:
    """
    # Base case - 1 item, nothing to sort!
    if len(arr) < 2:
        print("No sorting required, array: ", arr)
        return arr
    else:
        pivot_index = int(len(arr) / 2)
        pivot = arr[pivot_index]

        print("Array -> ", arr)
        print("Pivot value -> ", pivot)
        print("Pivot index -> ", pivot_index)

        arr.pop(pivot_index)

        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        print("[+] less -> ", less)
        print("[+] greater -> ", greater)
        print("\n\n")

        return quicksort(less) + [pivot] + quicksort(greater)


messy_arr = [5,3,6,1,7,4,3,4,5,2,8,10,12,1]

print(quicksort(messy_arr))
