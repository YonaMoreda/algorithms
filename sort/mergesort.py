import random


def merge_sort(ls):
    return ls if len(ls) <= 1 else merge(merge_sort(ls[:len(ls) // 2]), merge_sort(ls[len(ls) // 2:]))


def merge(xs, ys):
    return xs or ys if not xs or not ys else [xs[0]] + merge(xs[1:], ys) if xs[0] <= ys[0] else [ys[0]] + merge(xs, ys[1:])


def main():
    print(merge_sort([6, 2, 7, 9, 8, 22, 3, 2]))    # => [2, 2, 3, 6, 7, 8, 9, 22]
    print(merge_sort([random.randint(0, 100) for _ in range(100)]))


if __name__ == "__main__":
    main()
