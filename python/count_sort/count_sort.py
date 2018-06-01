def count_sort(to_sort):
    """
    :param to_sort: number in to_sort must be in range (0,9)
    :return: sorted to_sort
    """
    if not to_sort:
        return

    count_list = [0] * 10

    for num in to_sort:
        count_list[num] += 1

    for i in range(1, 10):
        count_list[i] += count_list[i-1]

    result = [0] * len(to_sort)
    for i in reversed(range(len(to_sort))):
        result[count_list[to_sort[i]] -1] = to_sort[i]
        count_list[to_sort[i]] -= 1

    return result
