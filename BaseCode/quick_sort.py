def quick(array):
    # 递归出口
    if len(array) < 2:
        return array

    else:
        pivot_index = 0  # 第一个元素作为pivot
        pivot = array[pivot_index]

        less_part = [
            i for i in array[pivot_index+1:] if i < pivot
        ]
        great_part = [
            i for i in array[pivot_index+1:] if i > pivot
        ]

        return quick(less_part) + [pivot] + quick(great_part)


def test_quick():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(quick(ll))


if __name__ == '__main__':
    test_quick()