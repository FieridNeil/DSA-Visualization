import random

# In place selection sort
def selection_sort(V):
    for k in range(len(V) - 1):
        least_index = k
        for i in range(k+1, len(V)):
            if V.v[i].t < V.v[least_index].t:
                least_index = i

        V.swap(least_index, k)
        # temp = V.v[least_index]
        # V.v[least_index] = V.v[k]
        # V./v[k] = temp
    return V
# End selection sort

# In place quick sort
def quick_sort(V):
    return inplace_quick_sort_range(V, 0, len(V))

def inplace_quick_sort_range(V, s, e):
    if (e-s) >= 2:
        lte, eqe = inplace_partition(V, s, e)
        inplace_quick_sort_range(V, s, lte)
        inplace_quick_sort_range(V, eqe, e)
    return V

def inplace_partition(V, s, e):
    pivot = V.v[random.randint(s, e-1)].t
    lte = s
    ges = e
    while lte < ges:
        if V.v[lte].t < pivot:
            lte += 1
        elif V.v[ges-1].t >= pivot:
            ges -= 1
        else:
            # swap(V[lte], V[ges-1])
            V.swap(lte, ges-1)

            lte += 1
    eqe = lte
    for i in range(ges, e):
        if V.v[i].t == pivot:
            # swap(V[eqe], V[i])
            V.swap(eqe, i)

            eqe += 1

    return lte, eqe
