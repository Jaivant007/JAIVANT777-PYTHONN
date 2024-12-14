def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Test cases
print(merge_sorted_lists([1,2,4], [1,3,4]))  
print(merge_sorted_lists([], []))            
print(merge_sorted_lists([], [0]))           
print(merge_sorted_lists([], [1, 2, 3, 4, 5]))  
print(merge_sorted_lists([0, 1, 9], [3, 4, 5]))  

