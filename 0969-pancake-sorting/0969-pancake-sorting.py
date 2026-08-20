class Solution(object):
    def pancakeSort(self, arr):
        flips = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))

            if max_idx == size - 1:
                continue

            if max_idx != 0:
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                flips.append(max_idx + 1)

            arr[:size] = arr[:size][::-1]
            flips.append(size)

        return flips
        