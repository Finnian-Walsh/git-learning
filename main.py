import statistics
import matplotlib.pyplot as plt

from random import randint
from time import perf_counter
from typing import Callable, Iterable, Optional, TypeVar

from lib import half_sort, merge


def merge_test():
    a = [1, 3, 4, 10]
    b = [1, 2, 3.5, 5, 6, 7]

    c = merge(a, b)

    print(c)


def half_sort_test(size: int) -> float:
    unsorted_list = []

    for _ in range(size):
        unsorted_list.append(randint(0, 1000))

    start = perf_counter()
    output = half_sort(unsorted_list)
    duration = perf_counter() - start

    assert output == sorted(unsorted_list), "Invalid test result"

    return duration * 1000


def half_sort_test_average(size: int, tests: int = 50) -> float:
    times = []

    for _ in range(tests):
        times.append(half_sort_test(size))

    return statistics.median(times)


X = TypeVar("X")
Y = TypeVar("Y")


def analyze_complexity(f: Callable[[X], Optional[Y]], domain: Iterable[X]):
    x_values = []
    y_values = []

    for x in domain:
        x_values.append(x)
        if y := f(x):
            y_values.append(y)
        else:
            break
    else:
        plt.plot(x_values, y_values)
        plt.savefig("complexity.png")


if __name__ == "__main__":
    analyze_complexity(half_sort_test_average, range(1000))
