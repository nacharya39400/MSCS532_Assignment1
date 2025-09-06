from typing import List, Union

# Accept ints and floats explicitly (a simple "array" of numbers).
Number = Union[int, float]


def insertion_sort(arr: List[Number]) -> List[Number]:
    """
    Sort a list *in place* into monotonically decreasing (non-increasing) order.

    The algorithm is stable: equal values keep their original relative order.
    Returns the same list object for convenience.

    Examples
    --------
    >>> insertion_sort([3, 1, 2, 2])
    [3, 2, 2, 1]
    >>> insertion_sort([])
    []
    >>> insertion_sort([5])
    [5]
    """
    n = len(arr)

    # Iterate over elements starting from index 1, treating the left side as the "sorted" region.
    for idx in range(1, n):
        current_value = arr[idx]   # The value we need to insert into the sorted region.
        scan_idx = idx - 1         # Start scanning from the element just left of current.

        # Shift elements that are *less than* current_value one position to the right.
        # Using "<" (not "<=") preserves stability for equal elements.
        while scan_idx >= 0 and arr[scan_idx] < current_value:
            arr[scan_idx + 1] = arr[scan_idx]
            scan_idx -= 1

        # Place current_value into the correct spot (first position where left element is >= it).
        arr[scan_idx + 1] = current_value

    return arr

