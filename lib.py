def half_sort(items):
    if len(items) > 1:
        half_index = len(items) // 2
        return merge(half_sort(items[0:half_index]), half_sort(items[half_index:]))
    else:
        return items


def merge(l1, l2):
    result = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        else:
            result.append(l1[i])
            i += 1

    result.extend(l1[i:])
    result.extend(l2[j:])

    return result
