def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(fill_slot, len(alist)):
            if alist[location] < alist[position_of_max]:
                position_of_max = location
            alist[fill_slot], alist[position_of_max] = alist[position_of_max], alist[fill_slot]