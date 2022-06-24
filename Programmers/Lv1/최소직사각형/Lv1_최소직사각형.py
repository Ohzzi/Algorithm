def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
