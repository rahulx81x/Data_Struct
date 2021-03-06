
# bubble ##################################

def bubble(el):
    size = len(el)
    for j in range(size - 1):
        flag = 0
        for i in range(size - 1 -j):
                if el[i] > el[i+1]:
                    el[i], el[i+1] = el[i+1], el[i]
                    flag = 1
        if flag != 1:
            break
    return el

# merge ###################################

def merge_func(l1, l2, res):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):   # for merging two sorted list
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    if i == len(l1):
        res += l2[j:]
    else:
        res += l1[i:]
    return res


def merge(el):
    if len(el) > 1:
        mid = len(el) // 2    # breaking into two
        left = el[:mid]
        right = el[mid:]

        left = merge(left)     #recursive func as long as every alement is not solo
        right = merge(right)

        el = merge_func(left, right, el)
    else:
        pass
    return el


# insertion ######################################
def insertion(el):
    for i in range(1,len(el)):
        pointer = el[i]
        j = i-1
        while j >= 0 and pointer < el[j]:
            el[j+1] = el[j]
            j -= 1
        el[j+1] = pointer
    return el

#selection ##################################################

def selection(el):
    for i in range(len(el)-1):
        min = i
        for j in range(i+1,len(el)):
            if el[j] < el[min]:
                min = j
        if i != min:
            el[i],el[min] = el[min], el[i]
    return el

# Quicksort #####################3
def quick(el):
    if len(el) <= 1:
        return el
    less_than_pivot=[]
    greater_than_pivot=[]
    pivot = el[0]
    for element in el[1:]:
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)
    return quick(less_than_pivot) + [pivot] + quick(greater_than_pivot)

