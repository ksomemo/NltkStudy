def my_merge(l1, l2):
    print 'merge start', l1, l2
    merge_list = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            merge_list.append(l1.pop(0))
        else:
            merge_list.append(l2.pop(0))
    if len(l1) == 0:
        merge_list += l2
    elif len(l2) == 0:
        merge_list += l1
    print 'merge end', merge_list
    return merge_list
 
def my_merge_sort(lst):
    lenlst = len(lst)
    if lenlst <= 1:
        return lst
    return my_merge(my_merge_sort(lst[:lenlst/2]), my_merge_sort(lst[lenlst/2:]))
