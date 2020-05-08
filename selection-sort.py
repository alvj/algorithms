"""
-----------------------------------------------
                SELECTION SORT!
-----------------------------------------------
"""


def main():
    unordered_arr = [12, 789 ,45, 36, 44, 75, 94, 18, 465, 210, 26, 40, 45, 69, 45, 22, 76, 42, 48, 7, 2, 6, 448, 12, 4, 9, 35, 68, 72, 84, 3, 1, 0, -10]

    print(selection_search(unordered_arr))

def selection_search(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index



if __name__ == "__main__":
    main()