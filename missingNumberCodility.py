# This is a demo task.
# Write a function:
# object Solution { def solution(a: Array[Int]): Int }
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
def solution(a):
    ordered_a = sorted(a)
    list_length = len(ordered_a)
    for j in range(1, list_length):
        if j not in ordered_a:
            return j
    return ordered_a[-1] + 1


print(solution([-2, -1, 0, 1, 2, 3, 4, 5, 6, 9]))
