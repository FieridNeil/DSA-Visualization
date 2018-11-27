import random
from vector import *
def in_place_selection_sort(V):
    for k in range(len(V) - 1):
        least_index = k
        for i in range(k+1, len(V)):
            if V[i] < V[least_index]:
                least_index = i
        V.swap(k, least_index)
    return V
#end selection sort

# def inplace_quick_sort(V):
#     return inplace_quick_sort_range(V, 0, len(V))
#
# def inplace_quick_sort_range(V, s, e):
#     if (e-s) >= 2:
#         lte, eqe = inplace_partition(V, s, e)
#         inplace_quick_sort_range(V, s, lte)
#         inplace_quick_sort_range(V, eqe, e)
#     return V
#
# def inplace_partition(V, s, e):
#     pivot = V[random.randint(s, e-1)]
#     lte = s
#     ges = e
#     while lte < ges:
#         if V[lte] < pivot:
#             lte += 1
#         elif V[ges-1] >= pivot:
#             ges -= 1
#         else:
#             V.swap(lte, ges-1)
#             # temp = V[lte]
#             # V[lte] = V[ges-1]
#             # V[ges-1] = temp
#             lte += 1
#     eqe = lte
#     for i in range(ges, e):
#         if V[i] == pivot:
#             V.swap(eqe, i)
#             # temp = V[eqe]
#             # V[i] = V[eqe]
#             # V[eqe] = temp
#             eqe += 1
#     return lte, eqe
#
#
# def sequential_search(V, q):
#     for i, e in enumerate(V):
#         V.add(i)
#         if e == q:
#             return e
#     return None
